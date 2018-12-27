from django.test import TestCase

from django.utils import timezone
import datetime

from blog.models import *
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from tagging.fields import TagField

class PostModelTests(TestCase):
    time = timezone.now() + datetime.timedelta(days=7)
    contents = Content(
        type='text',
        text='this is test',
        url='',
        created_date=time,
    )
    contents.save()
    post = Post(
        author=User.objects.get(id=2),
        category=Category.objects.get(id=3),
        contents=contents,
        title='test code3',
        tag='power!!',
        created_date=time,
    )
    post.save()


# class CommentModelTests(TestCase):
#     time = timezone.now() + datetime.timedelta(days=1)
