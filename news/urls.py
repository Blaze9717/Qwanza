from . import views
from django.urls import path 

#urls placed hear
urlpatterns = [
    path('',views.welcome,name="welcome"),
    path('',views.news_of_today,name="news_today"),
]


