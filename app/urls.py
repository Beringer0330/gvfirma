from os import name
from django.urls import path
from .views import index,services,blog,aboutUs,contact,team,error_404_view,detalleBlog,detalleEquipo,detalleService,landing,work
urlpatterns = [
    path('', index, name="index"),
    path('Service/', services, name="services"),
    path('Blog/', blog, name="blog"),
    path('Equipo/', team, name="team"),
    path('Nosotros/', aboutUs, name="aboutUs"),
    path('Contacto/', contact, name="contact"),
    path('Blogers/<slug:slug>/',detalleBlog,name="detalleBlog"),
    path('Equipo/<slug:my_id>/',detalleEquipo,name="detalleEquipo"),
    path('Service/<slug:su_id>/',detalleService,name="detalleService"),
    path('Landing-Page/', landing, name="landing"),
    path('Work/', work, name="work"),
]

