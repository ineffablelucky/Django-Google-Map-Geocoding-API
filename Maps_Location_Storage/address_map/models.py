from django.db import models
from django.contrib.gis.db import models


class Location(models.Model):

    name = models.CharField(max_length=100, blank=True)
    lat = models.PointField()
    lng = models.PointField()
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name
