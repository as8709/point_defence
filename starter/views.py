from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponse
from .models import Missile, MissileDesigns
from .forms import MissileForm
from django.core import serializers

import json

# Create your views here.
def index(request):
    return render(request, 'starter/index.html')

def designer(request):
    return render(request, 'starter/designer.html')

def missile_designer(request):
    designs = MissileDesigns.objects.all()
    missiles  = [(design.pk, design.design.name) for design in designs]
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
            "is_offensive" : lambda x: True if x == "on" else False,
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

        #add the new design
        MissileDesigns(design=missile).save()
        print("Making missle with pk {}".format(missile.pk))
        return JsonResponse(
            {"name" : missile.name,
            "id" : missile.pk
        })
    else:
         raise Http404()

def get_missile_design(request):
    if request.method == 'GET':
        design_id = request.GET.get("design_id")
        print("Getting missile with pk {}".format(design_id))
        missile = Missile.objects.get(pk=design_id)

        data = serializers.serialize('json', [missile])
        return HttpResponse(
            data,
            content_type="application/json"
        )
    else:
         raise Http404()

def gun_designer(request):
    raise Http404("Not implemented yet")

def controller_designer(request):
    raise Http404("Not implemented yet")