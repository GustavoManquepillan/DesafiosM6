from django.shortcuts import render, HttpResponseRedirect
from .models import Flan
from .forms import  ContactFormModelForm


def indice(request):
    #el contexto, es el diccionario donde se envian los datos
    # flanes = Flan.objects.all() #SELECT * FROM FLAN WHERE is_private=False
    public_flans = Flan.objects.filter(is_private=False)
    context = {
        'public_flans':public_flans
    }
    return render(request, 'index.html', context)


def acerca(request):
    return render(request, 'about.html', {})


def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True) #ORM Django Flan(tabla) objects filter, is_private=true
    #SELECT * FROM FLan WHERE is_private=True
    context = {
        'private_flans': private_flans
    }
    return render(request, 'welcome.html', context)


def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            # Guardar el formulario en la base de datos
            contact_form_instance = form.save()
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormModelForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


 
def exito(request):
    return render(request, 'exito.html')

