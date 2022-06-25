from django.shortcuts import redirect, render
from django.http import HttpResponse
from blogprincipal.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied


def home(request):
    return render(request, "blogprincipal/home.html")

def error(request):
    return render(request, "blogprincipal/error.html")

class BlogList(ListView):
    model = Blog
    template_name = "blogprincipal/listar.html"

class BlogDetalle(DetailView):
    model = Blog 
    template_name = "blogprincipal/detalle.html"

class BlogCrear(LoginRequiredMixin,CreateView):
    model = Blog
    success_url = "/blog/listar"
    template_name = "blogprincipal/crear.html"
    fields = ["titulo", "descripcion", "contenido", "image"]    

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class BlogActualizar(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Blog
    success_url = "/blog/listar"
    template_name = "blogprincipal/actualizar.html"
    fields = ["titulo", "descripcion", "contenido", "image"] 

    def test_func(self):
        exist = Blog.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
    def handle_no_permission(self):
        return  redirect("/blog/error") 
    

class BlogBorrar(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog
    success_url = "/blog/listar" 
    template_name = "blogprincipal/borrar.html"

    def test_func(self):
        exist = Blog.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False    
    def handle_no_permission(self):
        return  redirect("/blog/error") 


class BlogLogin(LoginView):
    template_name = 'blogprincipal/login.html'
    success_url = "/blog/home" 
    next_page = reverse_lazy("home")

class BlogLogout(LogoutView):
    template_name = 'blogprincipal/logout.html' 