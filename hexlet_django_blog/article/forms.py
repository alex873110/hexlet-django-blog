from django import forms # Импортируем формы Django
from django.forms import ModelForm
from .models import Article


class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий') # Текст комментария


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
