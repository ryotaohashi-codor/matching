from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['153.126.169.139']

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/usr/share/nginx/html/media'

# アップロードされたファイル、25Mぐらいまでは許容する
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440 * 10

# エラーなどが出た際のロギング。/var/log/django.logに保存
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"

        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/var/log/django.log',
            'formatter':'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
    },
}
