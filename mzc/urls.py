from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    path('',views.indexpage,name='index'),
    path('home/',views.homepage,name='home'),
    path('contact/',views.contactpage,name='contact')
]