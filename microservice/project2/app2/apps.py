from django.apps import AppConfig

class App2Config(AppConfig):
    name = 'app2'

    def ready(self):
        from django.core.management import call_command
        call_command('start_receiver')
