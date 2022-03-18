from xml.dom.minidom import Document
from django import template
from django.core.mail.message import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.http import Http404
from .models import Indicadores, Asociados,Testimonios,Blog,Categoria,TipoAso,clientesAsesorados,informacion,Blog_index,Frase,Service,sectoresAsesorados,carrusel
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string,get_template
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from .forms import LandingForm, FormWithCaptcha



from email.mime.application import MIMEApplication
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.

def error_404_view(request,exception):
    info = informacion.objects.all()
    data={
        'info':info,     
    }
    return render(request,'app/404.html',data)

def error_500_view(request):
    info = informacion.objects.all()
    data={
        'info':info,     
    }
    return render(request,'app/500.html',data)

def base(request):

    info = informacion.objects.all()
    data={
        'info':info,     
    }
    return render(request,'app/base.html',data)

def landing(request):
   
    testimonios = Testimonios.objects.all()
    clientes=clientesAsesorados.objects.all()
    info = informacion.objects.all()
    fra = Frase.objects.all()
    service = Service.objects.all()
    carru = carrusel.objects.all()
    data={
        'testimonios':testimonios,
        'clientes':clientes,  
        'info':info, 
        'fra':fra,
        'service':service,
        'carru':carru,
        'form': LandingForm(),
        'captcha':FormWithCaptcha, 
    }
    if request.method == 'POST':
        loginform=LandingForm(data=request.POST)
        if loginform.is_valid():
            loginform.save()
            subject = "Landing Page"
            name = request.POST['nombre']
            email = request.POST['correo']
            num = request.POST['numero']
            asunt = request.POST['asunto']

            context={'subject':subject,'name': name,'email': email,'num': num,'asunt': asunt}    
            template = get_template('app/correo/landing.html')
            content = template.render(context)
            
            email_from = settings.EMAIL_HOST_USER

            recipient_list=["gamarravasquez.firma@gmail.com","administracion@gvfirma.com","estefanysiempreteamare@gmail.com"]
            #"gamarravasquez.firma@gmail.com","administracion@gvfirma.com",
            message = EmailMultiAlternatives(subject,content,email_from,recipient_list)
            message.attach_alternative(content, 'text/html')
            message.send()

            messages.success(request," En breve se le estara contactando")
            return redirect(landing)
        else:
            data["form"]=loginform
            
    return render(request,'app/landingpage.html',data)
    
def index(request):
    if request.method == "POST":
        subject = "Agendar Consulta de Pagina Web"
        name = request.POST['name_ag']
        email = request.POST['email_ag']
       
        context={'subject':subject,'name': name,'email': email}    
        template = get_template('app/correo/agendar.html')
        content = template.render(context)
        
        email_from = settings.EMAIL_HOST_USER

        recipient_list=["estefanysiempreteamare@gmail.com"]
        #"gamarravasquez.firma@gmail.com","administracion@gvfirma.com",
        message = EmailMultiAlternatives(subject,content,email_from,recipient_list)
        message.attach_alternative(content, 'text/html')
        message.send()
        messages.success(request, 'Se agendo su consulta')
        return redirect('index')
    
    blog_index = Blog_index.objects.all()
    blog = Blog.objects.all()
    indicadores = Indicadores.objects.all()
    asociados = Asociados.objects.all()
    testimonios = Testimonios.objects.all()
    clientes=clientesAsesorados.objects.all()
    info = informacion.objects.all()
    fra = Frase.objects.all()
    service = Service.objects.all()
    carru = carrusel.objects.all()
    data={
        'indicadores':indicadores,
        'asociados':asociados,
        'testimonios':testimonios,
        'clientes':clientes,  
        'info':info, 
        'blog_index':blog_index,
        'blog':blog,
        'fra':fra,
        'service':service,
        'carru':carru,
    }
    return render(request,'app/index.html',data)

def services(request):
    info = informacion.objects.all()
    service = Service.objects.all()
    data={
        'service_page':"currentt",
        'service':service,
        'info':info,      
    }
    return render(request, 'app/services.html',data)

def blog(request):
    info = informacion.objects.all()
    blog = Blog.objects.all()
    categoria = Categoria.objects.all()
    data={
        'blog_page':"currentt",
        'blog':blog,
        'categoria':categoria,
        'info':info, 
    }
    return render(request, 'app/blog.html',data)

def team(request):
    info = informacion.objects.all()
    asociados = Asociados.objects.all()
    tipoasociado = TipoAso.objects.all()
    data={
        'team_page':"currentt", 
        'asociados':asociados,
        'tipoasociado':tipoasociado,
        'info':info, 
    }
    return render(request, 'app/team.html',data)

def aboutUs(request):
    info = informacion.objects.all()
    indicadores = Indicadores.objects.all()
    sectores=sectoresAsesorados.objects.all()
    servis=Service.objects.all()
    blog = Blog.objects.all()
    data={
        'nosotros_page':"currentt",
        'info':info,  
        'indicadores':indicadores, 
        'sectores':sectores, 
        'servis':servis,
        'blog':blog,
    }
    return render(request, 'app/aboutUs.html',data)

def contact(request):
    if request.method == "POST":
        subject = "Correo Contactanos de Pagina Web"
        name = request.POST['name_con']
        email = request.POST['email_con']
        message = request.POST['message_con']
        context= {'subject':subject, 'name': name,'email': email,'message':message}
        template = get_template('app/correo/correo.html')
        content = template.render(context)
        
        email_from = settings.EMAIL_HOST_USER

        recipient_list=["estefanysiempreteamare@gmail.com"]
    #"gamarravasquez.firma@gmail.com","administracion@gvfirma.com",
        #send_mail(subject,content,email_from,recipient_list)
        message = EmailMultiAlternatives(subject,content,email_from,recipient_list)
        message.attach_alternative(content, 'text/html')
        message.send()
        messages.success(request," En breve se le estara contactando")
        return redirect('contact')

        
    
    info = informacion.objects.all()
    data={
        'contacto_page':"currentt",
        'info':info,    
        'captcha':FormWithCaptcha, 
    }
    return render(request, 'app/contact.html',data)

def detalleBlog(request,slug):
    try:
        blog = Blog.objects.get(
        slug = slug
        )
    except Blog.DoesNotExist:
        raise Http404("Not Found")
    else:
        info = informacion.objects.all()
        blog = Blog.objects.get(slug = slug)
        data={
            'blog_page':"currentt",
            'db':blog,
            'info':info, 
        }    
        return render(request,'app/detalleblog.html',data)

def detalleEquipo(request,my_id):
    try:
        asociados = Asociados.objects.get(slug=my_id)
    except Asociados.DoesNotExist:
        raise Http404("Not Found")
    else:
        info = informacion.objects.all()
        asociados = Asociados.objects.get(slug=my_id)
        data={
            'team_page':"currentt", 
            'da':asociados,
            'info':info, 
        }
        return render(request,'app/detalleequipo.html',data)

def detalleService(request,su_id):
    try:
        service = Service.objects.get(slug=su_id)
    except Service.DoesNotExist:
        raise Http404("Not Found")
    else:
        if request.method == "POST":
            subject = "Servicios - Website"
            name = request.POST['name_ser']
            email = request.POST['email_ser']
            asunt = request.POST['asunto_ser']
            message = request.POST['message_ser']
            context= {'subject':subject, 'name': name,'email': email,'asunt':asunt,'message':message}
            template = get_template('app/correo/ser.html')
            content = template.render(context)
            
            email_from = settings.EMAIL_HOST_USER

            recipient_list=["estefanysiempreteamare@gmail.com"]
        #"gamarravasquez.firma@gmail.com","administracion@gvfirma.com",
            #send_mail(subject,content,email_from,recipient_list)
            message = EmailMultiAlternatives(subject,content,email_from,recipient_list)
            message.attach_alternative(content, 'text/html')
            message.send()
            messages.success(request, 'Se ha enviado su consulta')
            return redirect('detalleService', su_id)

        info = informacion.objects.all()
        service = Service.objects.get(slug=su_id)
        data={
            'service_page':"currentt", 
            'ds':service,
            'info':info, 
            'captcha':FormWithCaptcha, 
        }
        return render(request,'app/detalleservice.html',data)

def work(request):
    

    if request.method == "POST":
        subject = "Bolsa de Trabajo"
        name = request.POST['nombre']
        correo = request.POST['correo']
        numero = request.POST['numero']
        asunto = request.POST['asunto']
        context= {'subject':subject, 'name': name,'correo': correo,'numero': numero,'asunto':asunto}
        template = get_template('app/correo/working.html')
        content = template.render(context)
        
        email_from = settings.EMAIL_HOST_USER

        recipient_list=["estefanysiempreteamare@gmail.com"]
        #"gamarravasquez.firma@gmail.com","administracion@gvfirma.com",
        #send_mail(subject,content,email_from,recipient_list)
        message = EmailMultiAlternatives(subject,content,email_from,recipient_list)
        message.attach_alternative(content, 'text/html')
        message.send()

        messages.success(request, 'Por buscar ser parte del equipo, estamos evaluando tu solicitud')
        return redirect('work')

    info = informacion.objects.all()
    data={
        'nosotros_page':"currentt",
        'info':info,     
        'captcha':FormWithCaptcha,   
    }
    
    return render(request, 'app/work.html',data)