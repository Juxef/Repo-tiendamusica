from django.urls import path

from tiendamusica import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('guitarras/', views.guitarras, name="Guitarras"),
    path('amplificadores/', views.amplificadores, name="Amplificadores"),
    path('sucursales/', views.sucursales, name="Sucursales"),
    path('guitarraformulario/', views.guitarraformulario, name="GuitarraFormulario"),
    path('sucursalformulario/', views.sucursalformulario, name="SucursalFormulario"),
    path('amplificadorformulario/', views.amplificadorformulario, name="AmplificadorFormulario"),
    path('buscarmarca/', views.buscarmarca, name="BuscarMarca"),
    path('buscar/', views.buscar),  
     #   path('agregarguitarra/', views.agregarguitarra, name="AgregarGuitarra"),
 #   path('agregaramplificador/', views.agregaramplificador, name="AgregarAmplificador"),
 #   path('agregarsucursal/', views.agregarsucursal, name="AgregarSucursal"), 
]