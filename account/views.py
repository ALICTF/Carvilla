from django.shortcuts import redirect, render, reverse
from django.views.generic import CreateView, View
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .forms import SignupForm


class Login(View):
    template_name = 'registration/login.html'

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        user = auth.authenticate(self.request,
                                 username=self.request.POST.get('username'),
                                 password=self.request.POST.get('password'),
                                 )
        if user is not None:
            auth.login(self.request, user)
            return redirect('store:products')
        else:
            return redirect('account:login')


class Signup(SuccessMessageMixin, CreateView):

    model = get_user_model()
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('store:products')
    success_message = 'Your Are Login'
    
    def form_invalid(self, form):
        messages.error(self.request, 'Sorry, you are not registered on the site')
        return super().form_invalid(form)


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'You are logout')
    return redirect('login')

