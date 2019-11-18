from django.shortcuts import render
from articlesapp.models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all().order_by("-date")
    context = {
        'articles': articles,
        'title': 'News page'
    }
    return render(request, 'articlesapp/home.html', context=context)


def contacts(request):
    return render(request, 'articlesapp/contacts.html')
