from django.db import models

class Cryptocurrency(models.Model):
    crypto_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SantimentData(models.Model):
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    metric = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return f"{self.cryptocurrency.crypto_id} - {self.metric} - {self.datetime}"