from .base import *

SECRET_KEY = 'd9886f99-89bb-4687-a3e8-3b2a1efc774c'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
