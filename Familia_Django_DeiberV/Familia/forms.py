from django import forms

class FamiliarForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    cumpleanos = forms.DateField(label="Cumpleaños (año-mes-dia)")