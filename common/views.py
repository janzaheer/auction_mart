from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


class AccountLoginView(LoginView):
    template_name = 'common/login.html'

    def get_context_data(self, **kwargs):
        context = super(AccountLoginView, self).get_context_data(**kwargs)
        context.update({
            'name': 'Login'
        })
        return context


class AccountSignup(FormView):
    form_class = UserCreationForm
    template_name = 'common/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(user)
        return super(AccountSignup, self).form_invalid(form)

    def form_invalid(self, form):
        return super(AccountSignup, self).form_invalid(form)
