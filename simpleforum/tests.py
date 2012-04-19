from django_any import any_model
from django.core.urlresolvers import reverse
#from .models import Room
from django_webtest import WebTest

class ForumIndexTest(WebTest):

#   def setUp(self):
#       """
#       Initialization. Creating model instances for tests
#       """
#       self.root_room1 = any_model(Room, parent=None)
#       self.root_room2 = any_model(Room, parent=None)
#       self.child_room_1_1 = any_model(Room, parent=self.root_room1)
#       self.child_room_2_1 = any_model(Room, parent=self.root_room2)
#        pass

    def test_list_view(self):
        """
        Test that root rooms present in forum index list view
        """
        index_page = self.app.get(reverse("simpleforum_index"))
        self.assertEqual(index_page.status, '200 OK')

    def test_ololo(self):
        assert True
