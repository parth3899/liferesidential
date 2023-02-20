from .default import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://42960021855d4102b9200c40b45d8e3f@sentry.io/1435782",
    integrations=[DjangoIntegration()]
)

DEBUG = False
COMPRESS_ENABLED = False
# html minify is not caching correctly so is
# having a negative impact on performance, 
# so disabling until i can resolve.
HTML_MINIFY = True

#AREA Integration
APF_TOKEN = 'l6RchpeIBAGVoSWlmZUM5JP7VueiNUjdRW5nuz0as4c'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'lifewebsitedb21',
        'USER': 'lifeadmin',
        'PASSWORD': ',kNBMsbVjqb%6=Mu',
        'HOST': 'life-website-rds-ub18-dbinstance.csolxarqbqg2.eu-west-2.rds.amazonaws.com',
        'PORT': '5432',
        'CONN_MAX_AGE': 600,
    }
}


# AWS REMOTE STORAGE SETTINGS
AWS_STORAGE_BUCKET_NAME = 'liferesidential-life-website'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_CUSTOM_DOMAIN = 'd128szaucry5on.cloudfront.net'
AWS_S3_OBJECT_PARAMETERS = {
  'CacheControl': 'max-age=31536000',
}
#AWS_S3_SECURE_URLS = True

MEDIAFILES_LOCATION = 'media'
STATICFILES_LOCATION = 'static'

STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
COMPRESS_URL = STATIC_URL

DEFAULT_FILE_STORAGE = 'website.storages.MediaStorage'
STATICFILES_STORAGE = 'website.storages.CachedS3BotoStorage'
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
COMPRESS_STORAGE = STATICFILES_STORAGE


CACHES = {
    'default': {
       'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
       'LOCATION': 'cache_table',
       'TIMEOUT' : 60*60*24,
       'OPTIONS': {
           'MAX_ENTRIES': 10000,
       }
    }
}
