import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url  # مكتبة معتمدة لقراءة روابط قواعد البيانات الإنتاجية

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# تحميل الإعدادات المخفية من ملف .env في حال وجوده محلياً
load_dotenv(os.path.join(BASE_DIR, '.env'))

# الإعدادات الأمنية الديناميكية (آمنة للنشر والتطوير المحلي معاً)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-s+2p0a3xs64hs&e3_o+93bnah+v(ejgfia&ewoz4+bz=_w)kvt')

DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# السماح لجميع الروابط لضمان عمل السيرفر على ريندر دون مشاكل
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')


# التطبيقات المثبتة في المشروع
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # تطبيقاتنا الخاصة:
    'users.apps.UsersConfig',
    'correspondence.apps.CorrespondenceConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # الحزمة الأساسية لعرض الاستايلات والـ CSS على السيرفر
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# قاعدة البيانات: ذكية ومزدوجة تقرأ PostgreSQL من ريندر وتعمل بـ SQLite على جهازك المحلي
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}'
    )
}


# التحقق من قوة كلمات المرور
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


# اللغة والتوقيت الإداري للمشروع
LANGUAGE_CODE = 'ar' # الواجهة العربية الافتراضية
TIME_ZONE = 'Africa/Khartoum'
USE_I18N = True
USE_TZ = True


# إدارة الملفات الثابتة (Static Files CSS/JS) لبيئة الإنتاج والنشر
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ميزة تخصيص نموذج المستخدم وإعادة التوجيه بعد تسجيل الدخول
AUTH_USER_MODEL = 'users.UserProfile'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'


# إعدادات رفع وعرض المرفقات في النظام
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# الدعم البرمجي لـ ID الحقول تلقائياً
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
