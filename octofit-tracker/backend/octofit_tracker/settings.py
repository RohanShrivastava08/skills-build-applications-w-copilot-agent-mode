# Add 'rest_framework', 'corsheaders', and 'dj_rest_auth' to the INSTALLED_APPS list
INSTALLED_APPS = [
    # ...existing apps...
    'rest_framework',
    'corsheaders',
    'dj_rest_auth',
]

INSTALLED_APPS += [
    'corsheaders',
    'octofit_tracker',
]

# Add middleware for CORS headers
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing middleware...
]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# Configure CORS to allow all origins (adjust as needed for production)
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
]

# Allow all hosts
ALLOWED_HOSTS = ['*']

# Configure database to use Djongo for MongoDB
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}