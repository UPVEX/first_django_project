from django.http import HttpResponse

def index(request):
    return HttpResponse('welcome to my website')

def home(request):
    return HttpResponse('here is my web home')
