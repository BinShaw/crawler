from django.db import models
from abc import abstractmethod


# 爬虫基类，用作统一管理
class CrawlerBase(models.Model):
    # 基本信息
    _create_time = models.TimeField(name='create_time')
    _last_active_time = models.TimeField(name='active_time')
    _crawler_name = models.CharField(max_length=20, name='nick')

    # 爬虫功能相关
    _url = models.CharField(max_length=50)  # 入口URL
    _params = models.CharField(max_length=500)  # 携带参数
    _cookie = models.CharField(max_length=500)  # 携带cookie

    # 参数设置
    _always_do = models.SmallIntegerField(default=0)  # 循环执行，默认为否
    _interval_time = models.FloatField(default=0.5)  # 每次循环间隔时间，单位秒
    _is_random = models.SmallIntegerField(default=1)  # 是否随机爬去，默认为是

    # 定向爬取参数设置
    _depth = models.SmallIntegerField(default=3)  # 爬取深度，默认3
    _url_temporary_storage_id = 0  # 爬虫路径，默认从0开始，自行维护
    _current_crawler_storage_id = 0  # 当前爬虫缓存ID，自行维护

    # 设置基本参数
    def __init__(self, create_time, last_active_time, crawler_name, url, params, cookie):
        self._crawler_name = crawler_name
        self._create_time = create_time
        self._last_active_time = last_active_time
        self._url = url
        self._params = params
        self._cookie = cookie

    # 设置参数
    def set_params(self, always_do, interval_time, is_random):
        self._always_do = always_do
        self._interval_time = interval_time
        self._is_random = is_random

    # 设置定向爬取参数
    def set_direction_params(self, depth):
        self._depth = depth

    @abstractmethod  # 执行一次爬虫任务
    def do_crawler_thing(self):
        pass

    @abstractmethod  # 爬虫每次执行前准备工作，维护自己的爬虫路径
    def before_crawler_thing(self):
        pass

    @abstractmethod  # 爬虫每次执行后参数处理，维护自己的爬虫路径
    def after_crawler_thing(self):
        pass

    # 定向爬取--获得下一个爬虫
    def get_next_crawler(self):
        current_crawler = self.crawler_storage.filter(
            UrlTemporaryStorage.objects.get(id=self.current_crawler_storage_id)
        )
        return current_crawler.get_next_crawler_id()

    # 定向爬取--获得上一个爬虫
    def get_last_crawler(self):
        current_crawler = self.crawler_storage.filter(
            UrlTemporaryStorage.objects.get(id=self.current_crawler_storage_id)
        )
        return current_crawler.get_last_crawler_id()

    def is_random_crawler(self):
        if self.is_random == 0:
            return False
        else:
            return True


# 记录爬虫路径
class UrlTemporaryStorage(models.Model):
    _last_crawler_id = models.IntegerField(name='last_id')  # 上一个爬虫ID
    _next_crawler_id = models.IntegerField(name='next_id')  # 下一个爬虫ID
    _current_crawler = models.ForeignKey(CrawlerBase, related_name='crawler_storage')  # 当前爬虫

    def get_next_crawler_id(self):
        return self._next_crawler_id

    def get_last_crawler_id(self):
        return self._last_crawler_id

    @property
    def __str__(self):
        return_str = "Crawler[" + self._current_crawler.pk + "] between crawler[" \
                     + self._last_crawler_id + "] and crawler[" + self._next_crawler_id + "]"
        return return_str
