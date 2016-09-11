from django.db import models
import django.core.validators
from django.contrib.auth.models import User
# Create your models here.
class Missile(models.Model):
    #user = models.ForeignKey(User, editable=False)
    name = models.CharField(max_length=200)
    is_offensive = models.BooleanField()
    fuel = models.PositiveSmallIntegerField()
    thrust = models.PositiveIntegerField()
    rotation_force = models.PositiveIntegerField()
    radius = models.FloatField(validators=[django.core.validators.MinValueValidator(0)])
    length = models.FloatField(validators=[django.core.validators.MinValueValidator(0)])
    explosive_power = models.PositiveIntegerField()
    script = models.TextField()

    sensor_range = models.FloatField(validators=[django.core.validators.MinValueValidator(0)])
    sensor_resolution = models.FloatField(validators=[django.core.validators.MinValueValidator(0)])
    sensor_angle = models.FloatField(validators=[django.core.validators.MinValueValidator(0)])

class MissileDesigns(models.Model):
    design = models.ForeignKey(Missile, models.CASCADE)