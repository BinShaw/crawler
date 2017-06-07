from django.db import models


class RacingData(models.Model):
    termNum = models.IntegerField(name='term_num', primary_key=True)
    lotteryTime = models.TimeField(auto_now=True, name='lottery_time')
    n1 = models.SmallIntegerField()
    n2 = models.SmallIntegerField()
    n4 = models.SmallIntegerField()
    n5 = models.SmallIntegerField()
    n6 = models.SmallIntegerField()
    n7 = models.SmallIntegerField()
    n8 = models.SmallIntegerField()
    n9 = models.SmallIntegerField()
    n10 = models.SmallIntegerField()
