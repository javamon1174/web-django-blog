from django.contrib import admin
from .models import *

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Post Data', {
            'fields': ['category', 'author', 'title', 'tag', 'slug']
        }),
    )
    readonly_fields = ('created_date',)

    search_fields = ['category', 'title']
    ordering = ['created_date']
    list_filter = ('created_date',)

    inlines = [ContentInline, CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Content)