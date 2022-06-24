from django.urls import path

# trás tudo que está no arquivo views
from . import views

app_name = 'polls'
urlpatterns = [ # 'lista' de urls
    path('', views.index, name='index'), # chama de index a funcao index do views
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]