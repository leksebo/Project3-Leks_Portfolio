import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%%@hc$&j=ims#p6-yjff(ijz2_el#60^+h+-@ccf#4(-)_36)*'

# SECURITY WARNING: don't run with debug turned on in production!
# Set DEBUG based on environment, defaulting to True for development
DEBUG = os.environ.get('DJANGO_ENV') != 'production'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '[::1]',
    'led-portfolio-c2f377f40edc.herokuapp.com',
    'ancient-lemongrass-qi16rk8xa0ohhqf71fha6vba.herokudns.com'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'tinymce',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Only add SecurityMiddleware in production
if not DEBUG:
    MIDDLEWARE.insert(0, 'django.middleware.security.SecurityMiddleware')

ROOT_URLCONF = 'led_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'led_portfolio.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600
    )
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Only include the portfolio/static directory
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio/static'),
]

# Static files configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# WhiteNoise configuration
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ALLOW_ALL_ORIGINS = True
WHITENOISE_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# TinyMCE Configuration
TINYMCE_DEFAULT_CONFIG = {
    'height': 600,
    'width': 'auto',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
        advlist autolink lists link image charmap preview anchor
        searchreplace visualblocks code fullscreen
        insertdatetime media table paste code help wordcount
        emoticons save autosave codesample directionality nonbreaking
    ''',
    'toolbar': '''
        undo redo | formatselect | bold italic underline strikethrough |
        forecolor backcolor | alignleft aligncenter alignright alignjustify |
        bullist numlist outdent indent | removeformat | help | code |
        link image media | codesample | preview fullscreen
    ''',
    'toolbar_sticky': True,
    'autosave_ask_before_unload': True,
    'autosave_interval': '30s',
    'autosave_prefix': '{path}{query}-{id}-',
    'autosave_restore_when_empty': False,
    'autosave_retention': '2m',
    'menubar': 'file edit view insert format tools table help',
    'content_css': 'default',
    'image_advtab': True,
    'importcss_append': True,
    'image_caption': True,
    'noneditable_class': 'mceNonEditable',
    'paste_data_images': True,
    'relative_urls': False,
    'remove_script_host': True,
    'convert_urls': True,
    'browser_spellcheck': True,
    'contextmenu': 'link image table',
    'setup': '''function(editor) {
        editor.on('change', function () {
            editor.save();
        });
    }'''
}

# Security and Heroku Settings
if DEBUG:
    # Development settings
    SECURE_SSL_REDIRECT = False
    SECURE_PROXY_SSL_HEADER = None
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
else:
    # Production settings
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # Activate Django-Heroku only in production
    import django_heroku
    django_heroku.settings(locals())
    
    # Fix sqlite3 issue on Heroku
    options = DATABASES['default'].get('OPTIONS', {})
    options.pop('sslmode', None)
