from django import forms

class GuitarraFormulario(forms.Form):
    marca=forms.CharField()
    color=forms.CharField()
    precio = forms.IntegerField()

class AmplificadorFormulario(forms.Form):
    marca= forms.CharField()
    potencia= forms.CharField()
    precio= forms.IntegerField()

class SucursalFormulario(forms.Form):
    lugar= forms.CharField()
    direccion= forms.CharField()
    email= forms.EmailField()
    telefono= forms.CharField()

