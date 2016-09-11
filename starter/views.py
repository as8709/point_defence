from django.shortcuts import render
from django.http import Http404, Http403, JsonResponse, HttpResponse
from .models import Missile, MissileDesigns
from .forms import MissileForm
from django.core import serializers
from django.contrib.auth.decorators import login_required

import json

# Create your views here.
@login_required
def index(request):
    return render(request, 'starter/index.html')

@login_required
def designer(request):
    return render(request, 'starter/designer.html')

@login_required
def missile_designer(request):
    designs = MissileDesigns.objects.all()
    missiles  = [(design.design.pk, design.design.name) for design in designs]
    context = {
        'missiles' : missiles,
        'missile_form': MissileForm()
    }
    return render(request, 'starter/missile-designer.html', context)


def create_missile_design(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Http403()

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
        return JsonResponse(
            {"name" : missile.name,
            "id" : missile.pk
        })
    else:
         raise Http404()

def delete_missile_design(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Http403()
        design_id = request.POST.get("design_id")
        print(design_id)
        missile = Missile.objects.get(pk=design_id).delete()
        #the corresponding missile designs row should be deleted automatically
        return JsonResponse({})
    else:
         raise Http404()

def get_missile_design(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return Http403()
        design_id = request.GET.get("design_id")
        missile = Missile.objects.get(pk=design_id)

        data = serializers.serialize('json', [missile])
        return HttpResponse(
            data,
            content_type="application/json"
        )
    else:
         raise Http404()

@login_required
def gun_designer(request):
    raise Http404("Not implemented yet")

@login_required
def controller_designer(request):
    raise Http404("Not implemented yet")