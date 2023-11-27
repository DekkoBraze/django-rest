from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    token = models.ForeignKey('Token', on_delete=models.CASCADE, related_name='goods')


class Token(models.Model):
    token = models.CharField(max_length=36)

    def __str__(self):
        return self.token