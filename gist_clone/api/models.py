from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from rest_framework.reverse import reverse

class Gist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(null=True)
    timestamp = models.DateTimeField(default=datetime.now())
    starred = models.BooleanField(default=False)

    def __str__(self):
        return ''.join([self.title, ' by ', str(self.user)])

    def get_api_url(self, request=None):
        return reverse('gists-rud-view', kwargs={'pk': self.pk}, request=request)