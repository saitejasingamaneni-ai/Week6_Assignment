from django.shortcuts import render
from .models import Message

def home(request):
    return render(request, 'app/home.html')

def greet(request, name):
    return render(request, 'app/greet.html', {'name': name})

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'app/messages_list.html', {'messages': messages})

# Create your views here.
