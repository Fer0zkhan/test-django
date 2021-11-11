from django.urls import path
from .api_views import *

urlpatterns = [
    path('user-register', user_register_api_view, name='user-register'),
    path('user-login', user_login_api_view, name='user-login'),
    path('user-edit', update_user_api_view, name='user-update')
]
