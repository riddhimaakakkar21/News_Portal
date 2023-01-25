from .views import *
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ 
    path('signup', views.create_signup, name="create_signup"),
    path('login', views.Log_In, name="login"),
    path('index', views.index, name="index"),
    path('logout', views.Logout, name="Logout"),
    path('', views.HomeView, name="home"),
    path('dashboard', views.AddNews, name="add"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
