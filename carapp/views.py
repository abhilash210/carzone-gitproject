from django.shortcuts import render
from carapp.models import Team

# Create your views here.
def home(request):
    team=Team.objects.all()


    return render(request,'page/home.html',{'data':team})
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')

