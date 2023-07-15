from django.urls import path
from recruiter_app.views import *

urlpatterns = [
    path('recruiter-login/',recruiter_login_view,name='recruiter-login'),
]
