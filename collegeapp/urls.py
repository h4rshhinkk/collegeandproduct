from django.urls import path
from . import views
urlpatterns=[
    path('emea/',views.fncollege,name='college'),
    path('newcourse/',views.fncourse,name='course')
]