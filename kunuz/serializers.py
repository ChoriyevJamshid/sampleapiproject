from django.contrib.auth import get_user_model
from rest_framework import serializers
from kunuz.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )


class PostSerializer(serializers.ModelSerializer):

    category_title = serializers.StringRelatedField(source="category.title",
                                                    read_only=True)
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'summary',
            'content',
            'author',
            'category',
            'category_title',
            'views'
        )
        read_only_fields  = ['views',]


