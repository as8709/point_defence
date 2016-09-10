from django.forms import ModelForm
from .models import Missile

class MissileForm(ModelForm):
    class Meta:
        model = Missile
        fields = ['name', 'is_offensive', 'fuel', 'thrust', 'rotation_force',
        'radius', 'length', 'explosive_power', 'script', 'sensor_range', 'sensor_resolution', 'sensor_angle']
