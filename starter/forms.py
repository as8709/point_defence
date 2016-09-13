from django.forms import ModelForm
from .models import Missile
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class MissileForm(ModelForm):
    class Meta:
        model = Missile
        fields = ['name', 'is_offensive', 'fuel', 'thrust', 'rotation_force',
        'radius', 'length', 'explosive_power', 'script', 'sensor_range', 'sensor_resolution', 'sensor_angle']
