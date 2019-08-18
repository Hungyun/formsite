from django.urls import path
from . import views


urlpatterns=[
    path('',views.VerbListView.as_view(),name='verblist')

]
