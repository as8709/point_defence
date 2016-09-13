from django.shortcuts import render
from django.http import Http404, HttpResponseForbidden, JsonResponse, HttpResponse, HttpResponseRedirect
from .models import Missile, MissileDesigns
from .forms import MissileForm, UserForm
from django.core import serializers
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


# Create your views here.
@login_required
def index(request):
    return render(request, 'starter/index.html')

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
        #create the user then redirect to the index
        return HttpResponseRedirect("/")
    else:
        form = UserForm()
        return render(request, 'starter/register.html', {"form":form})


@login_required
def designer(request):
    return render(request, 'starter/designer.html')

@login_required
def missile_designer(request):
    designs = MissileDesigns.objects.all()
    missiles  = [(design.design.pk, design.design.name) for design in designs]
    context = {
        'designs' : missiles,
        'design_form': MissileForm()
    }
    return render(request, 'starter/missile-designer.html', context)

@require_http_methods(["POST"])
def create_missile_design(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

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

@require_http_methods(["POST"])
def delete_missile_design(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    design_id = request.POST.get("design_id")
    print(design_id)
    missile = Missile.objects.get(pk=design_id).delete()
    #the corresponding missile designs row should be deleted automatically
    return JsonResponse({})

@require_http_methods(["GET"])
def get_missile_design(request):

    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    design_id = request.GET.get("design_id")
    missile = Missile.objects.get(pk=design_id)

    data = serializers.serialize('json', [missile])
    return HttpResponse(
        data,
        content_type="application/json"
    )
@login_required
def gun_designer(request):
    raise Http404("Not implemented yet")

@login_required
def controller_designer(request):
    raise Http404("Not implemented yet")