from . import views
from django.urls import path 

#urls placed hear
urlpatterns = [
    path('',views.welcome,name="welcome"),
]

