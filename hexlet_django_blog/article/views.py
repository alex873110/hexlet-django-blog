from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse

tags = ['articles',]

def index(request, tag, article_id):
    return render(request, 'articles/index.html', context={'tag': tag, 
'article': article_id},)

class IndexView(View):

    def get(self, request, *args, **kwargs):
#        return HttpResponse(tags)
         return redirect(reverse('article', kwargs={'article_id': 42, 'tag': 'Python'}))
