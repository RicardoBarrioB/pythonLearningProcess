from django.apps import AppConfig


class PandasWebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pandas_web'

    def ready(self):
        import pandas_web.signals
