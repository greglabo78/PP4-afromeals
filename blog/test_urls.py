from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views

# Create your tests here.
class TestURLs(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, views.PostList)

    def test_post_detail_url_is_resolved(self):
        # We need to pass a slug to generate the URL
        url = reverse('post_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, views.post_detail)

    def test_comment_edit_url_is_resolved(self):
        # We need to pass a slug and comment_id to generate the URL
        url = reverse('comment_edit', args=['some-slug', 1])
        self.assertEquals(resolve(url).func, views.comment_edit)

    def test_comment_delete_url_is_resolved(self):
        # We need to pass a slug and comment_id to generate the URL
        url = reverse('comment_delete', args=['some-slug', 1])
        self.assertEquals(resolve(url).func, views.comment_delete)
