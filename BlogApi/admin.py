from django.contrib import admin
from .models import BlogPost, User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'is_published')
    list_filter = ('is_published', 'created_at', 'updated_at')
