import os

gettext = lambda s: s

DATA_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^$37s-=!9(%z!ll7lsl=w=1-qctbvjhbdb$0e2ies9x4oaf*gh'


ALLOWED_HOSTS = ['.liferesidential.co.uk']

ADMINS = (('WebDevAlerts', 'webdevalerts@liferesidential.co.uk'),)


AUTH_USER_MODEL = 'authentication.CustomUser'

# Application definition
ROOT_URLCONF = 'website.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#DATETIME
DATETIME_FORMAT = 'd F Y H:i'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR, 'website', 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'website.apps.navigation.context_processors.navigation',
                'website.apps.generic.context_processors.footer',
                'website.apps.generic.context_processors.site_processor',
                'website.apps.property.context_processors.property_processor',
                'website.apps.cookiebar.context_processors.cookiebar_processor',
                'website.apps.company.context_processors.company_processor',
            ],
            'loaders': [
                # ['django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    # 'django.template.loaders.eggs.Loader',
                # ]],
            ],
        },
    },
]


MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'website.apps.generic.middleware.AuthenticatedCookieMiddleware',
]

INSTALLED_APPS = [
    'djangocms_classic_admin_style',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    'website.apps.authentication',

    'cms',

    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'djangocms_link',
    'djangocms_transfer',
    'reversion',
    
    'axes',
    'compressor',
    'django.contrib.gis',
    'django.contrib.humanize',
    'django_social_share',
    'djangocms_page_sitemap',
    'hitcount',
    'leaflet',
    'polymorphic_tree',
    'mptt',
    'oauth2_provider',
    'parler',
    'polymorphic',
    'rest_framework',
    'robots',
    'storages',
    'taggit',
    'widget_tweaks',
    'import_export',

    'website',
    'website.apps.area',
    'website.apps.company',
    'website.apps.cookiebar',
    'website.apps.development',
    'website.apps.generic',
    'website.apps.forms',
    'website.apps.navigation',
    'website.apps.news',
    'website.apps.property',
    'website.apps.quiz',
    'website.apps.socialmeta',
    'website.apps.testimonial',
    'website.apps.transport',
    'website.apps.webp_img',
    'pwa'
]

LANGUAGES = (
    ('en', gettext('English')),
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('English'),
            'public': True,
            },
        ],
    'default': {
        'fallbacks': ['en',],
        'public': False,
        }
}

PARLER_LANGUAGES = {
    1: (
        {'code': 'en'},
    ),
    'default': {
        'fallbacks': ['en'],
    }
}

CMS_TEMPLATES = (
    ('home.html', 'Home'),
    ('internal.html', 'Internal'),
    ('standard_text.html', 'Standard Text'),
    ('standard_text_bottom.html', 'Standard Text with Bottom (used only for department pages)'),
)
CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}
CMS_PLUGIN_CACHE = False

#Import export functionality
#IMPORT_EXPORT_USE_TRANSACTIONS = True

# SECURITY SETTINGS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

# EASY THUMBNAIL
THUMBNAIL_QUALITY = 85
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif', 'webp')
THUMBNAIL_SUBDIR = 'versions'
FILER_ENABLE_LOGGING = True
FILER_DEBUG = True
# META
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

# JDBC
INTERBASE_DRIVER = 'interbase.interclient.Driver'
JDBC_CONNECTION_STRING = 'jdbc:interbase://51.143.227.105:45731/d:/Database/P2Gold data.ib'
INTERBASE_USERNAME = 'sysdba'
INTERBASE_PASSWORD = 'tpEksehbQ2z7'

# P2Gold
P2GOLD_S3_URL = 'https://s3-eu-west-1.amazonaws.com/liferesidential/'

# DEZREZ
DEZREZ_API_KEY = 'DA77AAFD-5404-48B4-8B66-0879FF6458BD'
DEZREZ_AGENT_ID = '1520'
DEZREZ_API_URL = 'https://www.dezrez.com/DRApp/DotNetSites/WebEngine/property/'

# REAPIT
# REAPIT_CLIENT_ID = 'liruser'
# REAPIT_PASSWORD = '723025ba71681dc3c4bc17e5dae08160'
# REAPIT_WSDL = 'https://webservice.reapit.net/lir/?wsdl'



REAPIT_CLIENT_ID = '67lliul8dl5hp2giprabg2922v'
# REAPIT_WSDL = 'https://connect.reapit.cloud/authorize?response_type=code'
REAPIT_SECRET = 't9g4kdim8r3l8frsgv0ah37qtvcfl6a1rfg0rnlnda6rlmm5vj7'
REAPIT_CUSTOMER = 'SBOX'
REAPIT_URL = 'https://platform.reapit.cloud'
REAPIT_TOKEN_URL = 'https://connect.reapit.cloud/token'


# REAPIT_CLIENT_ID = '67lliul8dl5hp2giprabg2922v'
# REAPIT_WSDL = 'https://connect.reapit.cloud/authorize?'

#EMAILS
EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.office365.com'
EMAIL_HOST = 'relay.sensical.net'
EMAIL_PORT = 587
#EMAIL_HOST_USER = 'O365_LifeWeb_Usr@liferesidential.co.uk'
EMAIL_HOST_USER = 'sb2751'
#EMAIL_HOST_PASSWORD = 'tuumadOtOfY$0!'
EMAIL_HOST_PASSWORD = 'biyv1V/a'
SERVER_EMAIL = 'noreply@liferesidential.co.uk'
DEFAULT_FROM_EMAIL = 'noreply@liferesidential.co.uk'
FALLBACK_ENQUIRY_EMAIL = 'info@liferesidential.co.uk'

# LEAFLET
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (51.507351, -0.127758),
    'DEFAULT_ZOOM': 11,
    # 'PLUGINS': {
    #     'forms': {
    #         'js': [
    #             'https://maps.googleapis.com/maps/api/js',
    #             os.path.join(STATIC_URL, 'life/js/leaflet-google.js')
    #         ],
    #         'auto-include': True,
    #     },
    # }
}

#GEODJANGO MAPPING
OPENLAYERS_URL = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js'

#PeopleHR
PEOPLEHR_BASE_URL = 'https://api.peoplehr.net/'
PEOPLEHR_API_KEY = '5a94b6c1-b42e-428c-9572-4fb31bf51b38'


LIFE_COLOUR_PALETTE = [
    'FF7700', # Orange
    '545759', # Grey
    '003B4B', # Petrol blue
    '009B87', # Teal
    '532D6D', # Plum
    'B01658', # Magenta
    'ECAA00', # Yellow
]

#CKEDITOR
CKEDITOR_SETTINGS = {
    'colorButton_colors': ','.join(LIFE_COLOUR_PALETTE),
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['Link', 'Unlink'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table', 'Blockquote'],
        ['Source'],
    ]
}

CKEDITOR_SETTINGS_NO_PARAGRAPH = {
    'autoParagraph': False,
}

TEXT_ADDITIONAL_TAGS = ('iframe',)
TEXT_ADDITIONAL_ATTRIBUTES = ('scrolling', 'allowfullscreen', 'frameborder')

# TAGGIT
TAGGIT_CASE_INSENSITIVE = True

# AXES
AXES_USERNAME_FORM_FIELD = "email"
AXES_LOGIN_FAILURE_LIMIT = 10
AXES_BEHIND_REVERSE_PROXY = True
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = 'errors/axes_lockout.html'
# unauthorised ip addresses are blocked
# at nginx, hence no need to handle here.
# If the below settings are enabled
# and a hacker can bypass nginx with
# ip, they'll be free to brute force.
# AXES_NEVER_LOCKOUT_WHITELIST = True
# AXES_IP_WHITELIST = ['89.197.3.140',]

# DJANGO COMPRESSOR
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
    'compressor.filters.template.TemplateFilter',
]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_REBUILD_TIMEOUT = 60*60*24*30 # 30 days
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False

# GOOGLE RECAPTCHA
RECAPTCHA_SECRET_KEY = '6LdimCUUAAAAAMfxBmpZr_HdsQTGnWephkObW3dd'
RECAPTCHA_SITE_KEY = '6LdimCUUAAAAAOpaOJ3QCgEiRI1dDe6YhugA6ayX'

# RATERAGENT
RATERAGENT_URL = 'http://www.rateragent.co.uk/widgets/xml/FObtiulV1odYvTCGbkp1UUBzYromkBSYotYrhAZ0'

# HITCOUNT
HITCOUNT_KEEP_HIT_ACTIVE = {'days': 1 }

# ROBOTS
ROBOTS_USE_HOST = False
# if i don't add the sitemap in this way, it doesn't have
# the correct protocol for some reason?!
ROBOTS_USE_SITEMAP = False
ROBOTS_SITEMAP_URLS = [
    'https://liferesidential.co.uk/sitemap.xml',
]

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    )
}

# API
API_ALLOWED_IPS = [
    '89.197.3.140',     # LiFE
    '52.56.107.116',    # AWS NAT Gateway
    '176.35.253.104',   # P2Gold
]

# LOGGING CONFIG
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'log.request': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/log-request.log"),
            'maxBytes': 16777216, # 16 mb
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'log.security': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/log-security.log"),
            'maxBytes': 16777216, # 16 mb
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'error_log_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/log-error.log"),
            'maxBytes': 16777216,  # 16 mb
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'form.error_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/log-error-forms.log"),
            'maxBytes': 16777216,  # 16 mb
            'backupCount': 2,
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['log.request'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['log.security'],
            'level': 'WARNING',
            'propagate': True,
        },
        'management_commands_error': {
            'handlers': ['error_log_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'forms_errors': {
            'handlers': ['form.error_log'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
COMPRESS_ROOT = STATIC_ROOT


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'website/static/life/js', 'serviceworker.js')
PWA_APP_NAME = 'LiFE Residential'
PWA_APP_DESCRIPTION = "London-based estate agents LiFE Residential offer services in lettings, sales and property management. We specialise in luxury newly-built property."
PWA_APP_THEME_COLOR = '#f18c32'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': 'website/static/life/img/images--logos/logo--life-residential.png',
        'sizes': '160x160'
    },
    {
        'src': 'website/static/life/img/images--logos/logo--life-residential.png',
        'sizes': '192x192'
    },
    {
        'src': 'website/static/life/img/images--logos/logo--life-residential.png',
        'sizes': '512x512'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': 'website/static/life/img/images--logos/logo--life-residential.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PAGE_SITEMAP_DEFAULT_CHANGEFREQ = 'monthly'
PAGE_SITEMAP_CACHE_DURATION = 0.5
PROPERTY_SITEMAP_PAGINATE_BY = 14
