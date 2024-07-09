from django.http import JsonResponse
from .tasks import send_task

def send_message(request):
    send_task({'message': 'Hello from dash sobhan '})
    return JsonResponse({'status': 'Message sent to dash hasan'})
