from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
from treep import views
app_name = 'treep'
urlpatterns = [
    path("", views.indexView.as_view(), name="index"),
    path("roteiro/",views.RoteiroList.as_view(),name="roteiro"),
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # n sei se é realmente necessario
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) #esse nem faz diferença