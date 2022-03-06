
from pathlib import Path
import os
import django_heroku
import sys
from django.core.mail import EmailMultiAlternatives

sys.modules['fontawesome_free'] = __import__('fontawesome-free')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Include BOOTSTRAP5_FOLDER in path
BOOTSTRAP5_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "bootstrap5"))
if BOOTSTRAP5_FOLDER not in sys.path:
    sys.path.insert(0, BOOTSTRAP5_FOLDER)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ii7u-c^7(&u86+pgngdf@1z$z)94&x-1rx1ug_*izi=e%-kh5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

###Add New
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.forum_core',
    'bootstrap5',
    'tinymce',
    'crispy_forms',
    'filebrowser',
    'fontawesome_free',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'Forum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',

            ],
        },
    },
]

WSGI_APPLICATION = 'Forum.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
##Added Manually
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Managing Media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# Settings for django-bootstrap-v5
CRISPY_TEMPLATE_PACK = 'bootstrap4'
BOOTSTRAP5 = {
    "error_css_class": "bootstrap5-error",
    "required_css_class": "bootstrap5-required",
    "javascript_in_head": True,
}

#TINYMCE

TINYMCE_JS_URL = os.path.join(STATIC_URL, "path/to/tiny_mce/tiny_mce.js")

###Bootrap



###eMail Congfig:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = 'rony807777@gmail.com'
EMAIL_HOST_PASSWORD = 'Rony807777@gmail'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


EMAIL_FILE_PATH = '/' # change this to a proper location


# Activate Django-Heroku.
django_heroku.settings(locals())



FORMAT_MODULE_PATH = [
    'apps.forum_core.formats',
]



######
AWS_ACCESS_KEY_ID = os.environ.get('AKIAXBABVM7AK5AY24HW')
AWS_SECRET_ACCESS_KEY = os.environ.get('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')
AWS_STORAGE_BUCKET_NAME = 'webpres'

AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

STATICFILES_STORAGE = 'apps.forum_core.storage.MediaStorage'
DEFAULT_FILE_STORAGE = 'apps.forum_core.storage.MediaStorage'

STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
######

# To set static for admin
#ADMIN_MEDIA_PREFIX = '/static/admin/'
#To allow django-admin collectstatic to automatically bellow:
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'



######
TINYMCE_JS_URL = os.path.join(STATIC_URL, "path/to/tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "path/to/tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }
#####