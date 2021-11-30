from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ['title', 'slug']


admin.site.register(Blog, BlogAdmin)
