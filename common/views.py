from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy


class AccountLoginView(LoginView):
    template_name = 'common/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(AccountLoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse('home'))

    def form_invalid(self, form):
        return super(AccountLoginView, self).form_invalid(form)


class AccountSignup(FormView):
    form_class = UserCreationForm
    template_name = 'common/signup.html'
    success_url = '/home'

    def form_valid(self, form):
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        return super(AccountSignup, self).form_invalid(form)


class Home(TemplateView):
    template_name = 'common/home.html'


class Logout(LogoutView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
