from django.http import JsonResponse
from .tasks import receive_task
import threading

# def send_message(request):
#     send_task({'message': 'Hello from project2'})
#     return JsonResponse({'status': 'Message sent'})

def receive_message(request):
    thread = threading.Thread(target=receive_task)
    thread.start()
    return JsonResponse({'status': 'Started receiving messages'})
