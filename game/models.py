from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=256)
    sell_value = models.IntegerField()
    buy_value = models.IntegerField()
