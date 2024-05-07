from django.apps import AppConfig


class CoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coapp'

    def ready(self):
        import coapp.signals
