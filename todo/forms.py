from django.forms import DateInput, ModelForm
# Importamos el modelo para poder usarlo
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('date',)
        widgets = {
            'estimated_end' : DateInput(attrs={'type' : 'date'}),
        }
    