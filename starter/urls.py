from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^designer$', views.designer, name='designer'),
    url(r'^designer/missile', views.missile_designer, name='missile-designer'),
    url(r'^designer/gun', views.gun_designer, name='gun-designer'),
    url(r'^designer/controller', views.controller_designer, name='controller-designer'),
    url(r'create_missile_design', views.create_missile_design),
    url(r'get_missile_design', views.get_missile_design),
    url(r'^$', views.index, name='index'),

]