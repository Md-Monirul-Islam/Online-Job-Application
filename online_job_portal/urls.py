from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job-app',include('job.urls')),
    path('admin-app/',include('admin_app.urls')),
    path('user-app/',include('user_app.urls')),
    path('recruiter-app/',include('recruiter_app.urls')),
]
