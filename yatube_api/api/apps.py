from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'          # важно именно 'api', а не 'api_yatube.api'
    verbose_name = 'API'
