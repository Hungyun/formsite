from django import forms
from django.forms import ModelForm
from googleform.models import Name
'''import 需與表格連結的model型態
form class 以ModelForm定義
'''
class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ('姓名','手機號碼','我要幾台iphone', '我想兌換的東西')
        CHOICES=[('1','1'),('2','2')]
        widgets = {
            '姓名': forms.TextInput(attrs={'class': 'titleclass'}),
            '手機號碼': forms.Textarea(attrs={'class': 'textclass'}),
            '我要幾台iphone': forms.RadioSelect(),
            '我想兌換的東西':forms.TextInput(attrs={'class': 'titleclass'})
            }
