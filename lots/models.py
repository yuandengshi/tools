from django.db import models


class Set(models.Model):
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)


class Lot(models.Model):
    name = models.CharField(max_length=128)
    set = models.ForeignKey(Set)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)
