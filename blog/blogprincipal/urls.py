from django.conf.urls.static import static
from django.urls import path
from blogprincipal import views

urlpatterns = [
    path("", views.home, name ="home"),
    path("listar/", views.BlogList.as_view(), name ="listar"),
    path("detalle/<pk>", views.BlogDetalle.as_view(), name ="detalle"),
    path("crear/", views.BlogCrear.as_view(), name ="crear"),
    path("actualizar/<pk>/", views.BlogActualizar.as_view(), name ="actualizar"),
    path("borrar/<pk>/", views.BlogBorrar.as_view(), name ="borrar"),
    path("entrar/", views.BlogLogin.as_view(), name="entrar"),
    path("salir/", views.BlogLogout.as_view(), name="salir"),
    path("error/", views.error, name="error"),
]