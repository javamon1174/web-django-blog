'''
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
'''

from django.test import TestCase

from blog.models import *
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from django.template.defaultfilters import slugify
from tagging.fields import TagField

g_time = timezone.now() + datetime.timedelta(days=7)
g_username = "tester"

class PostModelTests(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.test_user = User.objects.create(username=g_username)
        self.test_cate = Category.objects.create(name="testing", author=User.objects.get(username=g_username))

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_string_representation(self):
        post = Post(title="My post title")

        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)

    def test_post_creation(self):
        user = User.objects.get(username=self.test_user)
        category = Category.objects.get(author=User.objects.get(username=self.test_user))

        post = Post(
            author=user,
            category=category,
            title='test title!!',
            tag='power!!',
            created_date=g_time,
        )

        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)

    def test_get_post(self):
        post = Post.objects.create(author=self.test_user, category=self.test_cate, title="testing!!")
        data = Post.objects.get(author=self.test_user)

        self.assertEqual(post.__str__(), data.title)

    def test_update_post(self):
        Post.objects.create(author=self.test_user, category=self.test_cate, title="testing!!")
        data = Post.objects.get(author=self.test_user)

        data.title = 'power'
        data.save()

        data2 = Post.objects.get(author=self.test_user)

        self.assertEqual(data.title, data2.title)

    def test_delete_post(self):
        post = Post.objects.create(author=self.test_user, category=self.test_cate, title="testing!!")

        d_post = Post.objects.get(id=post.id)
        d_post.delete();


class ContentModelTests(TestCase):
    time = timezone.now() + datetime.timedelta(days=1)

    def setUp(self):
        # Setup run before every test method.
        self.test_user = User.objects.create(username=g_username)
        self.test_cate = Category.objects.create(name="testing", author=User.objects.get(username=g_username))
        self.post = Post.objects.create(author=self.test_user, category=self.test_cate, title="testing!!")

    def test_content_creation(self):
        contents = Content(
            post=self.post,
            type='text',
            description='this is test',
            url='',
            created_date=self.time,
        )

        self.assertTrue(isinstance(contents, Content))
        self.assertEqual(contents.__str__(), contents.type)


class CommentModelTests(TestCase):
    time = timezone.now() + datetime.timedelta(days=1)

    def setUp(self):
        # Setup run before every test method.
        self.test_user = User.objects.create(username=g_username)
        self.test_cate = Category.objects.create(name="testing", author=User.objects.get(username=g_username))
        self.post = Post.objects.create(author=self.test_user, category=self.test_cate, title="testing!!")

    def test_comment_creation(self):
        comment = Comment(
            post=self.post,
            author=self.test_user,
            text="test!!",
        )

        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.__str__(), comment.text)


class CategoryModelTests(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.test_user = User.objects.create(username=g_username)

    def test_category_creation(self):
        category = Category.objects.create(name="testing", author=User.objects.get(username=g_username))

        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), category.name)