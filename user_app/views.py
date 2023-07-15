from django.shortcuts import render

# Create your views here.
def user_login_view(request):
    return render(request,'userApp/user_login.html')



############### User Sign up view #################
def user_signup_view(request):
    return render(request,'userApp/user_signup.html')