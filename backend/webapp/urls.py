

from django.urls import path
from webapp import views#
#from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    #path('', login_required(views.home, login_url='login'), name='home'),
]