from django.shortcuts import render
from .models import Post
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView - when using separate views
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model


# Create your views here.


# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class UserList(ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
