from django.shortcuts import render, redirect
from Users.forms import LoginForm,RegisterForm
def Home(request):
    form = LoginForm()
    Register=RegisterForm()

    return render(request, 'Home.html', {'form': form,"Register":Register})
