from django.forms import ModelForm
from .models import NewsArticle


class NewsArticleForm(ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['name', 'news_text', 'author']