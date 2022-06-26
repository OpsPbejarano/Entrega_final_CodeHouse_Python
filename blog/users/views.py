from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from users.forms import UsuarioForm
from users.models import Avatar
# Create your views here.


class SingUpUser(CreateView):
    template_name = "users/crear_cuenta.html"
    success_url = reverse_lazy('entrar')
    form_class = UsuarioForm 
    success_message = " Se creo tu usuario en mi pagina web "

class UserPerfil(DetailView):
    model = User 
    template_name = "users/perfil.html"

class UserModificar(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "users/editar.html"
    fields = ['first_name','last_name','username', 'email',]

    def get_success_url(self):
      return reverse_lazy("perfil", kwargs={"pk": self.request.user.id})

class AvatarCrear(LoginRequiredMixin,CreateView):
    model = Avatar
    success_url = "/blog/perfil"
    template_name = "users/cargar_avatar.html"
    fields = ["blog", "image"]    

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)