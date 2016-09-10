from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Missile, MissileDesigns
from .forms import MissileForm

import json

# Create your views here.
def index(request):
    return render(request, 'starter/index.html')

def designer(request):
    return render(request, 'starter/designer.html')

def missile_designer(request):
    design_ids = MissileDesigns.objects.all()
    missiles  = [(design_id, Missile.objects.get(id=design_id).name) for design_id in design_ids]
    context = {
        'missiles' : missiles,
        'missile_form': MissileForm()
    }
    return render(request, 'starter/missile-designer.html', context)

def create_missile_design(request):
    if request.method == 'POST':
        #fields is "id_<field_name>" -> <field_data>
        #convert to "<field_name>" -> <field_data>
        convert_functions = {
            "name" : lambda x: x,
            "is_offensive" : lambda x: True if x == "true" else False,
            "fuel" : int,
            "thrust" : int,
            "rotation_force" : int,
            "radius" : float,
            "length" : float,
            "explosive_power" : int,
            "script" : lambda x :x,
            "sensor_range" : float,
            "sensor_resolution" : float,
            "sensor_angle" : float,
        }
        fields = {field_id[3:] : convert_functions[field_id[3:]](field_val) for field_id, field_val in request.POST.items() if field_id.startswith("id")}

        missile = Missile(**fields)
        missile.save()

        return HttpResponse(
            json.dumps({}),
            content_type="application/json"
        )
    else:
         raise Http404()

def gun_designer(request):
    raise Http404("Not implemented yet")

def controller_designer(request):
    raise Http404("Not implemented yet")