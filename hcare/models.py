from __future__ import unicode_literals
from django.db import models


class Message(models.Model):
    receiver = models.CharField(max_length=30, null=False)
    sender = models.CharField(max_length=30, null=False)
    message = models.TextField(max_length=1000)
    date = models.DateField(null=True)

    def __unicode__(self):
        return self.sender + '-' + self.receiver


class Doctor(models.Model):
    username = models.CharField(max_length=30, null=False, default="")
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    domain = models.CharField(max_length=30, null=False)
    image = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name + '-' + self.domain
