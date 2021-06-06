from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
import pdb
from .decorators import stop_authenticated_user

# User Registration
@stop_authenticated_user
def userRegistration(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # create user into the system
            return redirect('userAuthApp:user_login')   # redirect to login page

    context = {
        'title': 'User Registration',
        'form': form,
    }
    return render (request, 'authentication/registration.html', context)


# User Login
@stop_authenticated_user
def userLogin(request):
    form = LoginUserForm()

    if request.method == "POST":
        form = LoginUserForm(request=request, data=request.POST)
        if form.is_valid():
            usrName = form.cleaned_data.get('username')
            passwrd = form.cleaned_data.get('password')
            # print("Username: %s" % (usrName))
            # print("Password: %s" % (passwrd))
            # pdb.set_trace()
            user = authenticate(request, username=usrName, password=passwrd)
            if user is not None:
                login(request, user)
                # print("Login Successful! ************************************")
                return redirect ('todoApp:alltodos')
            else:
                # print("Invalid process-1! ************************************")
                return redirect ('userAuthApp:user_login')

    context = {
        'title': 'User Login',
        'form': form,
    }
    return render (request, 'authentication/login.html', context)


# User Logout
def userLogout(request):
    logout(request)
    return redirect ('userAuthApp:user_login')