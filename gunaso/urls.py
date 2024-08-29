from django.contrib import admin
from django.urls import path, include
from gunasoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gunasoapp/', include('gunasoapp.urls')),
    path('', views.home, name='home'),
]
