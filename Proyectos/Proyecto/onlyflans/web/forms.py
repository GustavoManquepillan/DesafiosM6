from django import forms
from django.forms import ModelForm
from .models import ContactForm

class ContactFormForm(forms.Form):
    customer_name = forms.CharField(max_length=64, label='Nombre')
    customer_email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
        labels = {
            'customer_name': 'Nombre',
            'customer_email': 'Email',
            'message': 'Mensaje',
        }
