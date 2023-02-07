from .base import *

SECRET_KEY = 'd9886f99-89bb-4687-a3e8-3b2a1efc774c'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf'
            }

        }
    }