from running_crawler.models import CrawlerBase


# 爬虫仓库，维护爬虫行为
class CrawlerWarehouse(object):
    _crawler_list = []  # 用于存放全部爬虫对象
    _new_crawler_list = []  # 新增加的爬虫对象

    # 向容器中放入一个爬虫
    def put_crawler(self, crawler_base):
        if type(crawler_base) != type(CrawlerBase):
            return False
        else:
            self._new_crawler_list.append(self, crawler_base)

    # 获取全部爬虫列表
    def get_crawler(self):
        return self._crawler_list

    # 开启所有爬虫
    def do_crawler_run(self):
        for crawler in self._crawler_list:
            crawler.before_crawler_thing(crawler)
            crawler.do_crawler_thing(crawler)
            crawler.after_crawler_thing(crawler)

    # 开启新增爬虫
    def do_new_crawler_run(self):
        for crawler in self._new_crawler_list:
            crawler.before_crawler_thing(crawler)
            crawler.do_crawler_thing(crawler)
            crawler.after_crawler_thing(crawler)
        self._crawler_list.extend(self._new_crawler_list)  # 将新增爬虫追加到原来的爬虫中
        self._new_crawler_list.clear()  # 清空新增爬虫列表

    # 加载数据库中所有爬虫
    def init_all_crawlers(self):
        crawler_list = CrawlerBase.objects.all()
        for crawler in crawler_list:
            self._crawler_list.append(crawler)
