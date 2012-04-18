import re
from django.core import mail
from django_webtest import WebTest
from django.utils.translation import ugettext_lazy as _, ugettext as __

class AuthTest(WebTest):

	def testLoginLinkPresentForAnonymousUser(self):
		page = self.app.get('/')
		assert _('login') in page

	def testLogoutLinkNotPresentForAnonymousUser(self):
		page = self.app.get('/')
		assert _('logout') not in page

#    fixtures = ['users.json']

#    def testLogoutAndLogin(self):
#        page = self.app.get('/', user='kmike')
#        page = page.click(_('logout')).follow()
#        assert _('logout') not in page
#        login_form = page.click(_('login'), index= 0).form
#        login_form['email'] = 'example@example.com'
#        login_form['password'] = '123'
#        result_page = login_form.submit().follow()
#        assert _('login') not in result_page
#        assert _('logout') in result_page