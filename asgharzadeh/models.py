from django.db import models


class NightName(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField(auto_now=True)
    end = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'NightName<{self.id}:"{self.name}">'


class Room(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    uri = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Room<{self.name}>'
