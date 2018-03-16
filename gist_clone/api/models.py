from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

class Gist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(null=True)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return ''.join([self.title, ' by ', str(self.user)])
