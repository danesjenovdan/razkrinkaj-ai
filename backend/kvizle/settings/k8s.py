from .base import *

DEBUG = bool(os.getenv("DJANGO_DEBUG", ""))

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "")

ALLOWED_HOSTS = ["api.kvizle.si"]
CSRF_TRUSTED_ORIGINS = ["https://api.kvizle.si"]
CORS_ALLOWED_ORIGINS = ["https://kvizle.si"]

WAGTAILADMIN_BASE_URL = "https://api.kvizle.si"

STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", BASE_DIR / "static")
STATIC_URL = os.getenv("DJANGO_STATIC_URL_BASE", "/static/")

# Storage backends temp variables
_msfs = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
_s3s = "storages.backends.s3.S3Storage"

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
STORAGES["staticfiles"]["BACKEND"] = _msfs

if os.getenv("DJANGO_ENABLE_S3", False):
    STORAGES["default"]["BACKEND"] = _s3s
    AWS_ACCESS_KEY_ID = os.getenv("DJANGO_AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY = os.getenv("DJANGO_AWS_SECRET_ACCESS_KEY", "")
    AWS_STORAGE_BUCKET_NAME = os.getenv("DJANGO_AWS_STORAGE_BUCKET_NAME", "djnd")
    AWS_DEFAULT_ACL = "public-read"
    AWS_QUERYSTRING_AUTH = False
    AWS_LOCATION = os.getenv("DJANGO_AWS_LOCATION", "kvizle")
    AWS_S3_REGION_NAME = "fr-par"
    AWS_S3_ENDPOINT_URL = "https://s3.fr-par.scw.cloud"
    AWS_S3_SIGNATURE_VERSION = "s3v4"
    AWS_S3_FILE_OVERWRITE = False
