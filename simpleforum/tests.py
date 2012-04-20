from django.utils.translation import ugettext_lazy as _
from django_any import any_model
from django.core.urlresolvers import reverse
from .models import Room
from django_webtest import WebTest

def _get_index_page_url():
    """
    shortcut for getting forum index page url. Encapsulates reverse urlresolver usage
    """
    return reverse("simpleforum_index")

def _get_add_room_url():
    """
    shortcut for getting forum add room form page url. Encapsulates reverse urlresolver usage
    """
    return reverse('simpleforum_add_room')

class ForumIndexTest(WebTest):
    """
    Testing proper forum index page presence
    """

    def setUp(self):
        """
        Initialization. Creating model instances for tests
        """
        self.root_room1 = any_model(Room, parent=None,
            title="root room 1 title", description = "root room 1 description")
        self.root_room2 = any_model(Room, parent=None, title="root room 2 title")
        self.child_room_1_1 = any_model(Room, parent=self.root_room1, title="child room 1 1 title")
        self.child_room_2_1 = any_model(Room, parent=self.root_room2, title="child room 2 1 title")

    def test_index_page_status(self):
        """
        Test that forum index page exists and shows properly.
        """
        index_page = self.app.get(_get_index_page_url())
        self.assertEqual(index_page.status, '200 OK')

    def test_index_page_rooms(self):
        """
        Test that forum index page contains only root rooms
        """
        index_page = self.app.get(_get_index_page_url())
        self.assertIn(self.root_room1.title, index_page)
        self.assertIn(self.root_room1.description, index_page)
        self.assertIn(self.root_room2.title, index_page)
        self.assertNotIn(self.child_room_1_1.title, index_page)
        self.assertNotIn(self.child_room_2_1.title, index_page)

class AddForumRoomTest(WebTest):
    """
    Testing "add forum room" forum behaving properely
    """
    def setUp(self):
        """
        Initialization. Creating model instances for tests
        """
       # self.room1=any_model(Room,id=2)
        room_id='2'
        pass

    def test_add_room_form(self):
        """
        Testing add room form works properely
        """
        form = self.app.get(_get_add_room_url()).forms['add_room_form']
        self.assertEqual(form['title'].value, _('new room'))
        form['title'] = 'test root room'
        form['description'] = 'test root room description'
        response = form.submit()
        self.assertEqual(response.status, '302 FOUND')
        response = response.follow()
        self.assertIn(_('room was successfully added'), response)
        added_room = Room.objects.get(title='test root room', description='test root room description')
        assert added_room #exists
        # then testing redirect results
        self.assertNotIn('add_room_form', response.forms)
        self.assertIn(added_room.title, response)
        self.assertIn(added_room.description, response)
        
    def test_adding_child_form(self):
      
        #form_page = self.app.get(reverse('simpleforum.views.add_room',kwargs={ 'parent_room_id': '2' }))
        #self.assertEqual(form_page.status, '200 OK')
        form = self.app.get(reverse('simpleforum.views.add_room',kwargs={ 'parent_room_id': '2' })).forms['add_room_form']
        parent_cadidate=Room.objects.get(id=2)
        self.assertEqual(form['title'].value, _('new room'))
        form['title'] = 'test root room'
        form['description'] = 'test root room description'
        response = form.submit()
        self.assertEqual(response.status, '302 FOUND')
        response = response.follow()
        self.assertIn(_('room was successfully added'), response)
        added_room = Room.objects.get(title='test root room', description='test root room description')
        assert added_room #exists
        # then testing redirect results
        self.assertEqual('parent',parent_cadidate)
        self.assertNotIn('add_room_form', response.forms)
        self.assertIn(added_room.title, response)
        self.assertIn(added_room.description, response)
        
    def test_room_presence(self):
        """
        Testing newly created room present on proper pages with proper urls
        """
        room1 = any_model(Room, title='sample room 1 from this test', description='sample room 1 description', parent=None)
        room1.save()
        room2 = any_model(Room, title='sample room 2 from this test', description='sample room 2 description', parent=room1)
        room2.save()
        index = self.app.get(_get_index_page_url())
        self.assertIn(room1.title, index)
        self.assertIn(room1.description, index)
        self.assertNotIn(room2.title, index)
        self.assertNotIn(room2.description, index)
        room1details = self.app.get(room1.get_absolute_url())
        self.assertIn(room1.title, room1details)
        self.assertIn(room1.description, room1details)
        room2details = self.app.get(room2.get_absolute_url())
        self.assertIn(room2.title, room2details)
        self.assertIn(room2.description, room2details)