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
            'starred',
            'timestamp',
        ]
        read_only_fields = ['user', 'timestamp']

    def validate_title(self, value):
        qs = Gist.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('This title has already been used')
        return value