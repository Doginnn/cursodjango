from django.shortcuts import render
from django.utils import timezone
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
         
    return render(request, 'blog/post_list.html', {'posts': posts})

class PostModelViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-title')

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES