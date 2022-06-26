from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from users import views

urlpatterns = [
    path("crear", views.SingUpUser.as_view(), name ="crear_usuario"),
    path("perfil/<pk>/", views.UserPerfil.as_view(), name ="perfil"),
    path("editar/<pk>", views.UserModificar.as_view(), name ="editar"),
    path("cargaravatar/<pk>", views.AvatarCrear.as_view(), name ="cargar_avatar"), 
]