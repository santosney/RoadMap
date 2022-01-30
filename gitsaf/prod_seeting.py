import dj_database_url
import dj_database_url
from gitsaf.settings import *

DEBUG = False
SECRET_KEY = 'django-insecure-*^^^0k27*u3#%fry@abb1c#ra$40i@2^g1=tgeqg_vn48k%+4p'

DATABASES['default'].update(dj_database_url.config(conn_max_age=600))

ALLOWED_HOSTS = [
    'https://roadmapsaf.herokuapp.com/',
    'localhost',
    '127.0.0.1'
]