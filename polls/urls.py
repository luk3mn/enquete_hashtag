from django.urls import path

# trás tudo que está no arquivo views
from . import views

urlpatterns = [ # 'lista' de urls
    path('', views.index, name='index'), # chama de index a funcao index do views
]