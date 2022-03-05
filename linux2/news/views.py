from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from news.models import News


class MainListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = dict()
        news = News.objects.all()
        context['news_list'] = news
        return context


class SingleListView(TemplateView):
    template_name = 'singlenews.html'

    def get_context_data(self, **kwargs):
        context = dict()
        try:
            article = News.objects.get(id=kwargs['pk'])
        except News.DoesNotExist:
            raise Http404
        context['news_blog'] = article
        return context

