from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create test user
        test_user1 = User.objects.create_user(username='melvin', password='melvin123')
        test_user1.save()

        # test data
        test_data = Post.objects.create(title='Hello', author=test_user1, body='body content')
        test_data.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'melvin')
        self.assertEqual(title, 'Hello')
        self.assertEqual(body, 'body content')
