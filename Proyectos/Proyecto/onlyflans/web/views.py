from django.shortcuts import render, HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Flan
from .forms import ContactFormModelForm

def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    context = {
        'public_flans':public_flans
    }
    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    context = {
        'private_flans': private_flans
    }
    return render(request, 'welcome.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form_instance = form.save()
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormModelForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

def exito(request):
    return render(request, 'exito.html')

class MiVistaProtegida(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'

def detalle_receta(request, nombre):
    # Lógica para obtener los detalles de la receta con el nombre proporcionado
    # Utiliza el nombre de la receta para obtener los detalles necesarios
    # Por ejemplo:
    try:
        flan = Flan.objects.get(slug=nombre)
        # Ahora puedes usar 'flan' para obtener los detalles de la receta
        return render(request, 'detalle_receta.html', {'flan': flan})
    except Flan.DoesNotExist:
        # Maneja el caso donde la receta no existe
        return HttpResponseNotFound("La receta no existe")




