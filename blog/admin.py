from django.contrib import admin
from .models import *

class CategoryInline(admin.TabularInline):
    model = Category

class ContentInline(admin.StackedInline):
    model = Content

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Post Data', {
            'fields': ['category','author','title', 'tag', 'slug']
        }),

    )
    readonly_fields = ('created_date',)

    search_fields = ['category','title']
    ordering = ['created_date']
    list_filter = ('created_date',)

    inlines = [ContentInline, CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Content)