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


class Market(models.Model):
    place = models.CharField(max_length=255)
    day = models.CharField(max_length=12)
    _from = models.CharField(max_length=5)
    _to = models.CharField(max_length=5)
    long = models.SmallIntegerField()
    lat = models.SmallIntegerField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    # nb_farmers = models.ForeignKey('NbFarmer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "market"
        ordering = ['city']

    def __str__(self):
        return self.place
