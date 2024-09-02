from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from gunasoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gunasoapp/', include('gunasoapp.urls')),
    path('', views.home, name='home'),
    path('reports/', views.report_final, name='report_final'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)