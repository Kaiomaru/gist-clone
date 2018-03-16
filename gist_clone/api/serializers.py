from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Gist

class GistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gist
        fields = [
            'pk',
            'user',
            'title',
            'text',
            'timestamp'
        ]
        read_only_fields = ['user']