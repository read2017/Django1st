from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform(request):
    all_message = UserMessage.objects.all()
    for message in all_message:
        print(message.name)
    return render(request,'message_form.html')