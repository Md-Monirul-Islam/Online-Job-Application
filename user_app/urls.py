from django.urls import path
from user_app.views import *

urlpatterns = [
    path('user-login/',user_login_view,name='user-login'),
    path('user-sign-up/',user_signup_view,name='user-sign-up'),
]
