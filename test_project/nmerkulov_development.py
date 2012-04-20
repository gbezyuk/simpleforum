from test_project.settings import *
import os

DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/test_project'

PROJECT_ROOT = '/home/ananas/web/simpleforum/simpleforum/'
SITE_ROOT = PROJECT_ROOT + 'test_project/'
MEDIA_ROOT = SITE_ROOT + 'media/'
STATIC_ROOT = SITE_ROOT + 'static/'

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'cover')

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': PROJECT_ROOT + 'dev.sqlite3',
	}
}

ADMINS = (('Grigory Bezyuk', 'gbezyuk@gmail.com'))
MANAGERS = ADMINS
