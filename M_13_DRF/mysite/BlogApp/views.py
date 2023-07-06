from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    template_name = 'BlogApp/article_list.html'
    context_object_name = 'articles'
    queryset = (
        Article.objects.defer('content', 'author__bio').
        select_related('author').
        select_related('category').
        prefetch_related('tags').all()
    )