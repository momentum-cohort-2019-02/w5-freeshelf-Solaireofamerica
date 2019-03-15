from freeshelf.settings import *

import django_heroku

DEBUG = False

django_heroku.settings(locals())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'freeshelf',
        'USER': 'freeshelf',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
