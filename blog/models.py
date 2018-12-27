from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from tagging.fields import TagField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    tag = TagField();
    created_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return ('blog_post_detail', (),
                {
                    'slug' :self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Content(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, default='')
    type = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    url = models.URLField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

