from django_any import any_model
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

    def test_list_view(self):
        """
        Test that root rooms present in forum index list view
        """
        
