from rest_framework import serializers
from articlesapp.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "text", "date", "author")


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "date", "author")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "is_active")
