from django.forms import ModelForm, forms
# Importamos el modelo para poder usarlo
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)