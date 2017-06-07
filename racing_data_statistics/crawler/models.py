from django.db import models


class UserInfo(models):
    name = models.CharField(max_length=200)
    gender = models.SmallIntegerField(default=1)  # 默认为男
    attention_num = models.IntegerField()  # '关注了'数量
    follow_num = models.IntegerField()  # '关注者'数量
    been_liked_num = models.IntegerField()  # 受到点赞数量
    attention_topic_num = models.IntegerField()  # '关注的话题'数量
    attention_column_num = models.IntegerField()  # '关注的专栏'数量
    attention_question_num = models.IntegerField()  # '关注的问题'数量
    attention_favorite_num = models.IntegerField()  # '关注的收藏夹'数量

