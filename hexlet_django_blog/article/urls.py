from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleCommentsView, ArticleFormCreateView

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<tag>/<int:article_id>/', views.index, name='article'),
    path('<int:id>/', ArticleView.as_view()),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
