from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from hexlet_django_blog.article.models import Article
from .forms import CommentArticleForm
from .forms import ArticleForm

# Create your views here.
from django.http import HttpResponse

# tags = ['articles',]

def index(request, tag, article_id):
    return render(request, 'articles/index.html', context={'tag': tag, 
'article': article_id},)

class IndexView(View):

    def get(self, request, *args, **kwargs):
         articles = Article.objects.all()[:15]
         return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleCommentsView(View):

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])

        return render(request, 'articles/comment.html', context={
            'comment': comment,
        })


class CommentArticleView(View):

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm() # Создаем экземпляр нашей формы
        return render(request, 'comment.html', {'form': form}) # Передаем нашу форму в контексте


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('articles') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})
