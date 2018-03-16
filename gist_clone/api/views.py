from rest_framework import generics
from .models import Gist
from .serializers import GistSerializer
from rest_framework import mixins
from django.db.models import Q

class GistsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    
    serializer_class = GistSerializer

    #def perform_create(self, serializer):
        #serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        qs = Gist.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) | Q(text__icontains=query)).distinct()
        return qs

class GistsRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GistSerializer
    queryset = Gist.objects.all()