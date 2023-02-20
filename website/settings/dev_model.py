# from .default import *
from .default_local import *


DEBUG = True
HTML_MINIFY = False
COMPRESS_ENABLED = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'django_extensions',
)

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False


ADMINS = (('Developer name', 'first_name.last_name@tremend.com'),)


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DATABASE_NAME', 'lifedb_dev'),
        'USER': 'lifeadmin',
        'PASSWORD': 'sjiPEx2g',
        'HOST': 'lr-postgres',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE


# OVERRIDE DEFAULT GOOGLE RECAPTCHA
RECAPTCHA_SECRET_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
RECAPTCHA_SITE_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'


# AWS REMOTE STORAGE SETTINGS
AWS_STORAGE_BUCKET_NAME = 'liferesidential-life-website-stage'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# MEDIAFILES_LOCATION = 'media'
# STATICFILES_LOCATION = 'static'
#
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# COMPRESS_URL = STATIC_URL
#
# DEFAULT_FILE_STORAGE = 'website.storages.MediaStorage'
# STATICFILES_STORAGE = 'website.storages.CachedS3BotoStorage'
# THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
# COMPRESS_STORAGE = STATICFILES_STORAGE


CACHES = {
    'default': {
       'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
