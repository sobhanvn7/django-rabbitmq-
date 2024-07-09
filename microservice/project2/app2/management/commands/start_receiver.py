from django.core.management.base import BaseCommand
from app2.tasks import receive_task

class Command(BaseCommand):
    help = 'Starts the RabbitMQ receiver'

    def handle(self, *args, **kwargs):
        receive_task()
