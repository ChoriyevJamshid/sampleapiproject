from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from kunuz import serializers
from kunuz.models import Category, Post
from kunuz.throttling import RandomRateThrottle, BurstRateThrottle
from kunuz.permissions import IsOwnerPermission


class CategoryListAPIView(generics.ListAPIView):
    # throttle_classes = [RandomRateThrottle]
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class PostListAPIView(generics.ListAPIView):
    throttle_classes = [BurstRateThrottle]
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_url_kwarg = 'post_id'

    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj


class PostCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsOwnerPermission]
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_url_kwarg = 'post_id'


class PostDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser, IsOwnerPermission]
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_url_kwarg = 'post_id'
