from django.contrib import admin

# Register your models here.
from .models import Article
from django.contrib.admin import DateFieldListFilter

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')
    search_fields = ['name', 'body']
    list_filter = (('timestamp', DateFieldListFilter),)


# admin.site.register(Article, ArticleAdmin)

