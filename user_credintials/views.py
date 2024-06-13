from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# signup
class signup(CreateView):
    form_class = RegisterForm
    template_name = "signup.html"
    success_url = reverse_lazy("signup")

    def form_valid(self, form):
        messages.success(
            self.request,
            'Your account has been created successfully. Please <a href="{}">Login</a>'.format(
                reverse_lazy("login")
            ),
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Sign Up"
        return context


# login
class user_login(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "login.html"

    # success_url = reverse_lazy('home')
    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Logged In")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Information incorrect")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


# logout
class user_logout(LogoutView):
    next_page = reverse_lazy("home")
    success_url = reverse_lazy('home') 
    def get_success_url(self):
        return reverse_lazy("home")


# @method_decorator(login_required, name='dispatch')
# class user_logout(LogoutView):
#     next_page = reverse_lazy('home')
#     def dispatch(self, request, *args, **kwargs):
#         messages.success(request, "logged out!")
#         return super().dispatch(request, *args, **kwargs)