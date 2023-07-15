from django.urls import path
from job.views import *

urlpatterns = [
    path('',home_view,name='home'),
]
