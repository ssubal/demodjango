"""adf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="Home"),
    path('contact/', views.contact_view, name="contacts"),
    path('about/', views.about_view, name="about"),
    path('apps/', views.apps_view, name="apps"),
    path('movies/', views.movies_info_view, name="movies"),
    path('faqs/', views.faqs_view, name="faqs"),
    path('apps1/', views.apps1_view, name="apps1")
]
