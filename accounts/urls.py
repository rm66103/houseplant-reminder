from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import path

from .views import ProfileView

urlpatterns = [
    path('login/', BaseLoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('profile/', ProfileView.as_view(), name='profile')
]