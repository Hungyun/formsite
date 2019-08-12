from django import forms
from django.forms import ModelForm
from googleform.models import Name
'''import 需與表格連結的model型態
form class 以ModelForm定義
'''
class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ('姓名','手機號碼','我要幾台iphone','驗證碼')
        CHOICES=[('1','1'),('2','2')]
        widgets = {
            '姓名': forms.TextInput(attrs={'class': 'titleclass'}),
            '手機號碼': forms.TextInput(attrs={'class': 'textclass'}),
            '我要幾台iphone': forms.SelectMultiple(),
            '驗證碼':forms.TextInput(attrs={'class': 'titleclass'})
            }
