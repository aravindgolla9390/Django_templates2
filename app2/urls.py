from django.urls import path
from app2.views import *
app_name='somthing2'
urlpatterns=[
    path('htmlfile1/',htmlfile1,name='htmlfile1'),
]