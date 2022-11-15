from django.apps import AppConfig

class KVConfig(AppConfig):
    name = 'keithvaluation'
    verbose_name = 'Keithvaluation'

    def ready(self):
        from .signals import clear_cache
