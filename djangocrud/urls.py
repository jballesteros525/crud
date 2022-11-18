"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from partidos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='name'),
    path('singup/', views.singup, name='singup'),
    path('partidos/', views.partidos, name='partidos'),
    path('partidos_completed/', views.partidos_completed, name='partidos_completed'),
    path('partidos/create/', views.create_partidos, name='create_partidos'),
    path('partidos/<int:partidos_id>/', views.partidos_detail, name='partidos_detail'),
    path('partidos/<int:partidos_id>/complete', views.complete_partidos, name='complete_partidos'),
    path('partidos/<int:partidos_id>/delete', views.delete_partidos, name='delete_partidos'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
