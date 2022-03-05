from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class NewsCategory(MPTTModel):
    """Категории новостей"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Категории новостей'
        verbose_name = 'Категория новостей'

    def __str__(self):
        return self.title


class Tags(models.Model):
    """Тэги"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title


class News(models.Model):
    """Новости"""
    author = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    description = models.TextField()
    poster = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags, related_name='tags')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news_cat')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'

    def __str__(self):
        return self.title

    def get_comment(self):
        return self.comment.all()


class Comment(models.Model):
    """Комментарии"""
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(News, related_name="comment", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'