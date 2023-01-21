from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Account

# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    def get_object(self):
        return self.request.user

    template_name = "accounts/profile.html"