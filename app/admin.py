from dataclasses import fields
from pyexpat import model
from django.contrib import admin
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.views import services
from .models import Asociados,Testimonios,Indicadores,Blog,Categoria,TipoAso,clientesAsesorados,informacion,Blog_index,Frase,carrusel,Service,sectoresAsesorados,Landing
# Register your models here.

class AsociadosAdmin(admin.ModelAdmin):
    list_display = ["nombre_corto","nombre","slug","TipoAsociado","descripcion","imagen","foto"]
    search_fields = ["nombre"]
    list_editable = ["TipoAsociado"]
    def foto(self, obj):
        return format_html('<img src={} width="100" height="100" />', obj.imagen.url)

class TestimoniosAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion","imagen","foto"]
    search_fields = ["nombre"]
    def foto(self, obj):
        return format_html('<img src={} width="100" height="100" />', obj.imagen.url)
    #list_per_page=5

class IndicadoresAdmin(admin.ModelAdmin):
    list_display = ["nombre","valor"]
    list_editable = ["valor"]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]

class Blog_indexAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]

class FraseAdmin(admin.ModelAdmin):
    list_display = ["nombre","autor"]
    search_fields = ["nombre"]
    list_editable = ["autor"]

class CarruselAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion","foto"]
    search_fields = ["nombre"]
    def foto(self, obj):
        return format_html('<img src={} width="100" height="100" />', obj.imagen.url)
    
    
class TipoAsoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]

class clientesAsesoradosAdmin(admin.ModelAdmin):
    list_display = ["nombre","imagen","foto"]
    search_fields = ["nombre"]
    def foto(self, obj):
        return format_html('<img src={} width="100" height="100" />', obj.imagen.url)

class sectoresAsesoradosAdmin(admin.ModelAdmin):
    list_display = ["nombre","imagen","foto"]
    search_fields = ["nombre"]
    def foto(self, obj):
        return format_html('<img src={} width="100" height="100" />', obj.imagen.url)

class BlogAdmin(admin.ModelAdmin):
    list_display = ["nombre","lugar","autor","categoria","fecha","imagen","foto"]
    list_editable = ["autor","categoria","lugar"]
    search_fields = ["nombre"]
    def foto(self, obj):
        return format_html('<img src={} width="100" height="100" />', obj.imagen.url)
    

class informacionAdmin(admin.ModelAdmin):
    list_display = ["nombre","telefono","correo","direccion","navbar","footer"]
    list_editable = ["telefono"]
    search_fields = ["nombre"]
    def navbar(self, obj):
        return format_html('<img src={} width="100" height="50" />', obj.logo_nav.url)
    
    def footer(self, obj):
        return format_html('<img src={} width="100" height="50" />', obj.lofo_footer.url)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["nombre","icono","icono_blanco","foto","slug"]
    search_fields = ["nombre"]
    def icono(self, obj):
        return format_html('<img src={} width="100" height="50" />', obj.icon.url)
    
    def icono_blanco(self, obj):
        return format_html('<img src={} width="100" height="50" />', obj.icon_white.url)
    
    def foto(self, obj):
        return format_html('<img src={} width="100" height="50" />', obj.imagen.url)

class LandingResources(resources.ModelResource):
    class Meta:
        model = Landing
        
class LandingAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["fecha","nombre","correo","numero","asunto"]
    search_fields = ["nombre"]
    resources_class = LandingResources


        
    

    
admin.site.register(Asociados,AsociadosAdmin)
admin.site.register(Testimonios,TestimoniosAdmin)
admin.site.register(Indicadores,IndicadoresAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(TipoAso,TipoAsoAdmin)
admin.site.register(clientesAsesorados,clientesAsesoradosAdmin)
admin.site.register(sectoresAsesorados,sectoresAsesoradosAdmin)
admin.site.register(informacion,informacionAdmin)
admin.site.register(Blog_index,Blog_indexAdmin)
admin.site.register(Frase,FraseAdmin)
admin.site.register(carrusel,CarruselAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Landing,LandingAdmin)
