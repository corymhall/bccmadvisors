from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"), 
    path('mn-terms.html', views.mnterms, name="mnterms"),
    path('afro-terms.html', views.afroterms, name="afroterms"),
    path('africafund.html', views.africafund, name="africafund"),
    path('smcap.html', views.smcap, name="smcap"),
]   