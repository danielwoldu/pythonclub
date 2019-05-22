from django.shortcuts import render
from .models import Resource, Meeting, MeetingMinute

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getresource(request):
    resources=Resource.objects.all()
    return render(request,'clubapp/resources.html',{'resources':resources})