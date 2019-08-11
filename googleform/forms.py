from django.forms import ModelForm
from googleform.models import Name
'''import 需與表格連結的model型態
form class 以ModelForm定義
'''
class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = '__all__'
