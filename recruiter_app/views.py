from django.shortcuts import render

# Create your views here.
def recruiter_login_view(request):
    return render(request,'recruiterApp/recruiter_login.html')