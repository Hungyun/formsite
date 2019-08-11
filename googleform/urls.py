from django.urls import path
from googleform import views


urlpatterns=[
    path('inputyourname/',views.get_name,name='formpage'),
#連結的name用於template tagging可直接呼叫
    path('',views.index,name='homepage'),
]
