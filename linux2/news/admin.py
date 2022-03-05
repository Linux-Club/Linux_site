from django.contrib import admin
from news.models import NewsCategory, News

from news.models import Tags


@admin.register(NewsCategory)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class CategoryNewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Tags)
class CategoryNewsAdmin(admin.ModelAdmin):
    pass
