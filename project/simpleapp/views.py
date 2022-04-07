from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import NewsArticle
from .filters import NewsArticleFilter
from .forms import NewsArticleForm


class NewsListView(ListView):
    model = NewsArticle
    ordering = '-news_data'
    template_name = 'simpleapp/news_list.html'
    context_object_name = 'articles'
    paginate_by = 1
    form_class = NewsArticleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewsArticleForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class NewsListSearch(ListView):
    model = NewsArticle
    ordering = '-news_data'
    template_name = 'simpleapp/news_search.html'
    context_object_name = 'articles'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsArticleFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsDetail(DetailView):
    model = NewsArticle
    template_name = 'simpleapp/news_detail.html'
    context_object_name = 'article'


class NewsCreateView(CreateView):
    template_name = 'simpleapp/news_create.html'
    form_class = NewsArticleForm


class NewsEditView(UpdateView):
    template_name = 'simpleapp/news_edit.html'
    form_class = NewsArticleForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return NewsArticle.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    template_name = 'simpleapp/news_delete.html'
    context_object_name = 'article'
    queryset = NewsArticle.objects.all()
    success_url = '/news/'






