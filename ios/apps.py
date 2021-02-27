from django.apps import AppConfig


class IosConfig(AppConfig):
    name = 'ios'

    def ready(self):
        from ios import signals
