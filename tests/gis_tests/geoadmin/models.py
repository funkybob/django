from django.contrib.gis import admin
from django.contrib.gis.db import models


class City(models.Model):
    name = models.CharField(max_length=30)
    point = models.PointField()

    objects = models.GeoManager()

    class Meta:
        app_label = 'geoadmin'

    def __str__(self):
        return self.name

admin.site.register(City, admin.OSMGeoAdmin)
