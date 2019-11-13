from django.urls import path
from .views import *

urlpatterns = [
    path('listar/', doadores_list, name="doadores_list"),
    path('cadastrar/', doadores_create, name="doadores_create"),
    path('atualizar/<int:id>/', doadores_update, name="doadores_update"),
    path('apagar/<int:id>/', doadores_delete, name="doadores_delete"),
]