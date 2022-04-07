from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    name = models.CharField(max_length=128)
    news_data = models.DateField(auto_now_add=True)
    news_text = models.TextField()
    author = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.news_data} {self.name} {self.news_text} {self.author}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

