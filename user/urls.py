from django.urls import path
from .views import *

app_name = "user"
urlpatterns = [
    path("", view=UserListView.as_view(), name="listar y crear usuarios"),
    path("<int:pk>/", view=UserDetailView.as_view(), name="Detalle de un usuario"),
    path("movies/", view=MovieListView.as_view(), name="listar y crear peliculas"),
    path("movies/<int:pk>/", view=MovieDetailView.as_view(), name="detalle de una pelicula"),
    path("compras/", view=User_has_MovieListView.as_view(), name="listar y crear las compras"),
    path("compras/<int:pk>/", view=User_has_MovieDetailView.as_view(), name="listar una compra")
]