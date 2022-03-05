from django.contrib import admin
from post.models import PostCategory, Posts


@admin.register(PostCategory)
class PostsAdmin(admin.ModelAdmin):
    pass


@admin.register(Posts)
class CategoryPostAdmin(admin.ModelAdmin):
    pass
