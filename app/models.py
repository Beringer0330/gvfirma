from enum import auto
from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.signals import pre_save
from webSite.utils import unique_slug_generator
from django.core.mail import EmailMessage
# Create your models here.

class Indicadores(models.Model):
    nombre=models.CharField(max_length=50)
    valor = models.IntegerField()
    def __str__(self):
        return self.nombre

class TipoAso(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre


class Asociados(models.Model):
    nombre_corto= models.CharField(max_length=40)
    nombre = models.CharField(max_length=90)
    descripcion = models.TextField()
    vida = RichTextField()
    TipoAsociado = models.ForeignKey("TipoAso",on_delete=models.CASCADE, null= False)
    imagen = models.ImageField(upload_to="asociados", null=True)
    slug =models.SlugField('Slug', max_length=150,blank=True, null=True)
    linkedin = models.CharField(max_length=200)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Testimonios(models.Model):
    nombre = models.CharField(max_length=90)
    descripcion = RichTextField('Descripcion' ,max_length=600)
    imagen = models.ImageField(upload_to="testimonios", null=True)

    def __str__(self):
        return self.nombre

#-------------P-o-s-t------------------------- 
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class carrusel(models.Model):
    nombre = models.CharField('Titulo' ,max_length=150)
    descripcion= models.TextField('Descripcion' ,max_length=150,null=True,blank=True)
    imagen = models.ImageField(upload_to="carrusel", null=True)
    def __str__(self):
        return self.nombre


class Frase(models.Model):
    nombre = RichTextField('Frase' ,max_length=600)
    autor = models.ForeignKey("Asociados",on_delete=models.CASCADE, null= False)
    def __str__(self):
        return self.nombre

class Blog(models.Model):
    nombre = models.CharField('Titulo' ,max_length=150)
    body = RichTextField()
    imagen = models.ImageField(upload_to="blog", null=True)
    autor = models.ForeignKey("Asociados",on_delete=models.CASCADE, null= False)
    categoria = models.ForeignKey("Categoria",on_delete=models.CASCADE, null= False)
    fecha = models.DateTimeField( auto_now=True, auto_now_add=False)
    lugar = models.ForeignKey("Blog_index",on_delete=models.CASCADE, null= True,default=3)
    slug =models.SlugField('Slug', max_length=150,blank=True, null=True)
    def __str__(self):
        return self.nombre

class clientesAsesorados(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="clientes", null=True)
    def __str__(self):
        return self.nombre

class sectoresAsesorados(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="sectores", null=True)
    def __str__(self):
        return self.nombre

class informacion(models.Model):
    favicon = models.ImageField(upload_to="Favicon", null=True)
    nombre = models.CharField(max_length=50)
    telefono = models. CharField(max_length=12)
    direccion = models.CharField(max_length=250)
    correo = models.EmailField()
    logo_nav = models.ImageField(upload_to="Navbar", null=True)
    lofo_footer = models.ImageField(upload_to="Footer", null=True)
    intro_nosotros = RichTextField()
    mision = models.TextField(max_length=235)
    vision = models.TextField(max_length=235)
    facebook = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    url_maps= models.TextField(max_length=600)
    url_video= models.CharField(max_length=200)


class Blog_index(models.Model):
    nombre = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre

class Service(models.Model):
    nombre= models.CharField(max_length=40)
    info= models.TextField(max_length=600)
    descripcion = RichTextField()
    icon = models.ImageField(upload_to="services_icon", null=True)
    icon_white = models.ImageField(upload_to="services_icon", null=True)
    imagen = models.ImageField(upload_to="services", null=True)
    slug =models.SlugField('Slug', max_length=150,blank=True, null=True)


class Landing(models.Model):
    nombre= models.CharField(max_length=40)
    correo= models.CharField(max_length=600)
    numero= models.IntegerField()
    asunto= models.TextField(max_length=600)
    fecha = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

    



def slug_generator_Service(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator_Service, sender=Service)

def slug_generator_Blog(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator_Blog, sender=Blog)

def slug_generator_Asociados(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator_Asociados, sender=Asociados)

