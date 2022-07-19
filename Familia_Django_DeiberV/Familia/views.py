from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from .forms import FamiliarForm
from .models import Familiar

def inicio(request):

    if request.method ==  'POST':
        form = FamiliarForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            cumpleanos = form.cleaned_data['cumpleanos']

            familiar_nuevo = Familiar(nombre=nombre,edad=edad,cumpleanos=cumpleanos)
            familiar_nuevo.save()
            return HttpResponseRedirect("./familiares/")
            
    else:
        form = FamiliarForm()

    return  render(request,'index.html',{'formFamiliares': form})


def familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request,'familiares.html',{'familiares':lista_familiares})