from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)
    dept = models.SmallIntegerField()
    long = models.SmallIntegerField()
    lat = models.SmallIntegerField()

    class Meta:
        verbose_name = "city"
        ordering = ['dept', 'name']

    def __str__(self):
        return self.name
