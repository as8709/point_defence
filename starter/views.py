from django.shortcuts import render
from django.http import Http404
# Create your views here.
def index(request):
    return render(request, 'starter/index.html')

def designer(request):
    return render(request, 'starter/designer.html')

def missile_designer(request):
    raise Http404("Not implemented yet")

def gun_designer(request):
    raise Http404("Not implemented yet")

def controller_designer(request):
    raise Http404("Not implemented yet")