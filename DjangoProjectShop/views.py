from django.shortcuts import render, redirect
from Users.forms import LoginForm,RegisterForm
from Category.models import Category
def Home(request):
    form = LoginForm()
    Register=RegisterForm()

    return render(request, 'Home.html', {'form': form,"Register":Register})

