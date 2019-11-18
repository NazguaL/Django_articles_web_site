from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from articlesapp.models import Article
from articlesapp.serializers import ArticleSerializer, ArticlesSerializer, UserSerializer


class ArticleView(APIView):

    def get(self, request, pk):
        article = ArticleSerializer(
            Article.objects.get(id=pk),
            many=False,
            context=request
        ).data

        return Response({"article": article})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()

        return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)


class ArticlesView(APIView):

    def get(self, request):
        articles = ArticleSerializer(
            Article.objects.all().order_by("-id"),
            many=True,
            context=request
        ).data

        return Response({"articles": articles})

    def post(self, request):
        article = request.data.get('article')

        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})


class UserWiew(APIView):

    def get(self, request):
        users = UserSerializer(
            User.objects.all().order_by("-id"),
            many=True,
            context=request
        ).data

        return Response({"users": users})
