INSTALLED_APPS = [
    'photo.apps.PhotoConfig',
	...
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = 'media/'
# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'