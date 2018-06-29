from django.db import models  # not used and gis.db.models takes over
from django.contrib.gis.db import models


class Location(models.Model):

    name = models.CharField(max_length=100, blank=True)
    coordinate = models.PointField(srid=4326)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name
