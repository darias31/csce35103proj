# photon_project/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'photon',
        'USER': 'postgres',
        'PASSWORD': 'student',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
