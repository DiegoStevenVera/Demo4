from django.urls import path
from .views import *

app_name="administrator"
urlpatterns = [
    path('administrator/', view=AdministratorListView.as_view(), name="listar administradores"),
    path('administrator/<int:pk>/', view=AdministratorDetailView.as_view(), name="detalle del administrador")
]