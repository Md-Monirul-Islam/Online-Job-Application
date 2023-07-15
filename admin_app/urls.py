from django.urls import path
from admin_app.views import *

urlpatterns = [
    path('admin-login/',admin_login_view,name='admin-login'),
]
