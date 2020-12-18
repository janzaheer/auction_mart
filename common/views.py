from django.db import transaction
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate, logout
from common.forms import RegisterForm
from auction.forms import CompanyForm


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
    form_class = RegisterForm
    template_name = 'common/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Would register user along with company
        """
        with transaction.atomic():
            form.save()
            username = self.request.POST['username']
            password = self.request.POST['password1']

            company_name = form.cleaned_data.get('company_name')
            company_address = form.cleaned_data.get('company_address')
            company_kwargs = {
                'name': company_name,
                'address': company_address,
            }
            company_form = CompanyForm(company_kwargs)
            if company_form.is_valid():
                company_form.save()

            # authenticate user then login
            user = authenticate(username=username, password=password)
            login(self.request, user)
        return super(AccountSignup, self).form_valid(form)

    def form_invalid(self, form):
        return super(AccountSignup, self).form_invalid(form)


class Home(TemplateView):
    template_name = 'common/home.html'


class Logout(LogoutView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
