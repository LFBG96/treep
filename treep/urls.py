from django.urls import path
from treep.views import Create

from . import views
from django.conf.urls.static import static
from django.conf import settings
from treep import views
from .views import RoteiroList
app_name = 'treep'
urlpatterns = [
    path("", views.indexView.as_view(), name="index"),
    path("roteiro/",RoteiroList,name="roteiro"),
    path("criar/",Create,name="criar"),
    path("delete/<int:pk>/",views.RoteiroDelete.as_view(),name="roteiroDelete"),
    path("login/",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    path("cadastro/",views.cadastro, name = "cadastro"),
    

    #path("a/",Create, name="a"),
    #path('b/',Lista),
    
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # n sei se é realmente necessario
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) #esse nem faz diferença