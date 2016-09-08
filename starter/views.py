from django.shortcuts import render
from django.http import Http404
from .models import Missile, MissileDesigns

# Create your views here.
def index(request):
    return render(request, 'starter/index.html')

def designer(request):
    return render(request, 'starter/designer.html')

def missile_designer(request):
    design_ids = MissileDesigns.objects.all()
    missiles  = [(design_id, Missile.objects.get(id=design_id).name) for design_id in design_ids]
    context = {
        'missiles' : missiles
    }
    return render(request, 'starter/missile-designer.html', context)

def gun_designer(request):
    raise Http404("Not implemented yet")

def controller_designer(request):
    raise Http404("Not implemented yet")