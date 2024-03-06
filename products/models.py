from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name