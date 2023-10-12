from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()


class Token(models.Model):
    token = models.CharField(max_length=36)