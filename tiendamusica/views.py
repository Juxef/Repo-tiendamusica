from django.shortcuts import render
from django.http import HttpResponse
from tiendamusica.models import Guitarra, Amplificador, Sucursal
from django.template import loader
from tiendamusica.forms import GuitarraFormulario, AmplificadorFormulario, SucursalFormulario


# Create your views here.
"""
def agregar(request, nom, ed, fecha):
    familiar = Familiar(nombre=nom, edad = ed, fechanac = fecha)
    familiar.save()
    texto = f"Se guardo en la BD el familiar: {familiar.nombre}, edad: {familiar.edad}, Fecha de nac: {familiar.fechanac}"
    return HttpResponse(texto)
"""
"""

Primeras inicializaciones de prueba

def agregarguitarra(request):

      guitarra =  Guitarra(marca="Yamaha Pacifica 012", color="Negro", precio="65000")
      guitarra.save()
  
def agregaramplificador(request):

      amplificador =  Amplificador(marca="Fender Champion", potencia="20W", precio="42000")
      amplificador.save()
  
def agregarsucursal(request):

      sucursal =  Sucursal(lugar="Paraná, Entre Ríos", direccion="Av. Almafuerte 1324", email="parana@tiendamusica.com.ar", telefono="4339878")
      sucursal.save()
"""

def inicio(request):

      return render(request, "inicio.html")

def guitarras(request):
    guitarras = Guitarra.objects.all()
    dicc = {"guitarras":guitarras}
    plantilla = loader.get_template("guitarras.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def amplificadores(request):

      ampli = Amplificador.objects.all()
      dicc = {"amplificadores":ampli}
      plantilla = loader.get_template("amplificadores.html")
      documento = plantilla.render(dicc)
      return HttpResponse(documento)
 

def sucursales(request):

      suc = Sucursal.objects.all()
      dicc = {"sucursales":suc}
      plantilla = loader.get_template("sucursales.html")
      documento = plantilla.render(dicc)
      return HttpResponse(documento)


def guitarraformulario(request):
    if request.method == 'POST':
        miForm = GuitarraFormulario(request.POST)

        if miForm.is_valid():
            data = miForm.cleaned_data

            guitarra = Guitarra(marca=data['marca'], color=data['color'], precio=data['precio'])
            guitarra.save()

            return render(request,"inicio.html")

    else:
        miForm = GuitarraFormulario()
    
    return render(request, "guitarraformulario.html", {"miForm":miForm})

def amplificadorformulario(request):
    if request.method == 'POST':
        miForm = AmplificadorFormulario(request.POST)

        if miForm.is_valid():
            data = miForm.cleaned_data

            ampli = Amplificador(marca=data['marca'], potencia=data['potencia'], precio=data['precio'])
            ampli.save()

            return render(request,"inicio.html")

    else:
        miForm = AmplificadorFormulario()
    
    return render(request, "amplificadorformulario.html", {"miForm":miForm})


def sucursalformulario(request):
    if request.method == 'POST':
        miForm = SucursalFormulario(request.POST)

        if miForm.is_valid():
            data = miForm.cleaned_data

            suc = Sucursal(lugar=data['lugar'], direccion=data['direccion'], email=data['email'], telefono=data['telefono'])
            suc.save()

            return render(request,"inicio.html")

    else:
        miForm = SucursalFormulario()
    
    return render(request, "sucursalformulario.html", {"miForm":miForm})

def buscarmarca(request):
    return render(request, "buscarmarca.html")

def buscar(request):
    if request.GET["marca"]:
#   respuesta = f"Estoy buscando la guitarra: {request.GET['guitarra']}"
        marca = request.GET['marca']
        guitarras = Guitarra.objects.filter(marca__icontains= marca)
        amplificadores = Amplificador.objects.filter(marca__icontains= marca)
       
        dicc = {"guitarras":guitarras}
        dicc2 = {"amplificadores":amplificadores}
        dicc3 = {"marca":marca}
        dicc.update(dicc2)
        dicc.update(dicc3)
        print(dicc)
        return render(request, "resultadobusqueda.html", dicc)
    
    else:
        respuesta = "No enviaste los datos"

    return HttpResponse(respuesta)

