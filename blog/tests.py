from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

# Create your tests here.
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user(username='testuser', password='12345')
        Post.objects.create(
            title='A unique title',
            slug='a-unique-slug',
            author=user,
            content='Some content',
            excert='A short excerpt'
        )

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_string_representation(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'The title of this post is {post.title}'
        self.assertEqual(str(post), expected_object_name)


    def test_ordering(self):
        user = User.objects.get(username='testuser')
        Post.objects.create(title='Second Post', slug='second-post', author=user, content='Another content')
        first_item = Post.objects.all()[0]
        self.assertEqual(first_item.title, 'Second Post')

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='commenter', password='12345')
        post_user = User.objects.create_user(username='postuser', password='54321')
        post = Post.objects.create(title='Test Post', slug='test-post', author=post_user, content='Test Post Content')
        Comment.objects.create(post=post, author=user, body='A comment here')

    def test_comment_content(self):
        comment = Comment.objects.get(id=1)
        expected_body = 'A comment here'
        self.assertEqual(comment.body, expected_body)

    def test_comment_approval_default(self):
        comment = Comment.objects.get(id=1)
        self.assertFalse(comment.approved)

    def test_string_representation(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'Comment {comment.body} by {comment.author}'
        self.assertEqual(str(comment), expected_object_name)

  

