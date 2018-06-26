from django.db import models


# Create your models here.
class Location(models.Model):

    name = models.CharField(max_length=100)
    lat = models.DecimalField('Latitude', max_digits=10, decimal_places=8)
    lng = models.DecimalField('Longitude', max_digits=11, decimal_places=8)
    address = models.CharField(max_length=500,  null=True, blank=True)
    city = models.CharField(max_length=100,  null=True, blank=True)
    state = models.CharField(max_length=100,  null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name


