import main

from unittest import TestCase
from unittest.mock import patch


class TestBlog(TestCase):
    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
                'body': 'quia et suscipit\nsuscipit recusandae consequunt ur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

        assert MockBlog is main.Blog
        assert MockBlog.called
        blog.posts.assert_called_with()
        blog.posts.assert_called_once_with()
        blog.reset_mock()
        blog.posts.assert_not_called()
