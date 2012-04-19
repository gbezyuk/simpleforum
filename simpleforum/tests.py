from django_any import any_model
from django.core.urlresolvers import reverse
from .models import Room
from django_webtest import WebTest

class ForumIndexTest(WebTest):

    def setUp(self):
        """
        Initialization. Creating model instances for tests
        """
        self.root_room1 = any_model(Room, parent=None)
        self.root_room2 = any_model(Room, parent=None)
        self.child_room_1_1 = any_model(Room, parent=self.root_room1)
        self.child_room_2_1 = any_model(Room, parent=self.root_room2)

    def _get_index_page(self):
        return self.app.get(reverse("simpleforum_index"))

    def test_index_page_status(self):
        """
        Test that forum index page exists and shows properly.
        """
        index_page = self._get_index_page()
        self.assertEqual(index_page.status, '200 OK')

    def test_index_page_rooms(self):
        """
        Test that forum index page contains only root rooms
        """
        index_page = self._get_index_page()
        self.assertIn(self.root_room1.title, index_page)
        self.assertIn(self.root_room2.title, index_page)
        self.assertNotIn(self.child_room_1_1.title, index_page)
        self.assertNotIn(self.child_room_2_1.title, index_page)