from django_webtest import WebTest

class IndexPageTest(WebTest):

    def test_index_view(self):
        """
        Test index page opens with Http 200 OK status
        """
        index_page = self.app.get('/')
        self.assertEqual(index_page.status, '200 OK')