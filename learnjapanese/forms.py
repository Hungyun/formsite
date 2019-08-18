from django import forms
from .models import Verb

class NewVerbForm(forms.ModelForm):

    class Meta:
        model = Verb
        fields = '__all__'

        widgets={
            'name':forms.TextInput(),
        }
