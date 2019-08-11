'''views.py的功能主要為定義網頁中
需使用的一些function與html檔案的連結
處理
'''
from django.shortcuts import render
# from django.http import HttpResponse
# from googleform.models import Name
from googleform.forms import NameForm
#從forms.py import 欲填寫的表格
#轉移給view中處理使用

# Create your views here.
def index(request):
    return render(request,'index.html')

def thankyoupage(request):
    return render(request,'thanks.html')

def get_name(request):
    form = NameForm()

    if request.method=='POST':
        form = NameForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thankyoupage(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'name.html',{'form':form})
