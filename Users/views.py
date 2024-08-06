from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .forms import  PasswrodChangeForm
from django.views.generic import  DeleteView
from  Users.models import  CustomeUser
from .forms import LoginForm,EditProfileForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin



def LoginView(request):
    form=LoginForm(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            Mobile=form.cleaned_data['Mobile']
            Password=form.cleaned_data['Password']
            user=authenticate(mobile=Mobile,password=Password)
            if user is not None:
                login(request,user)

                return  JsonResponse({"result":"success"})

            return  JsonResponse({'result':'error'})
    return  render(request, 'Home.html',{'form':form})


def RegisterView(request):
    Register=RegisterForm()
    if request.method == 'POST':
        Register=RegisterForm(request.POST)
        if  Register.is_valid():
            password =  Register.cleaned_data['Password']
            user = CustomeUser.objects.filter(mobile= Register.cleaned_data['mobile']).first()
            if user :
                return  JsonResponse({'reponse':'found'})
            else:
                user1 = Register.save(commit=False)
                user1.set_password(password)
                user1.save()
            return redirect('/')

    return render(request,"Home.html",{' Register': Register})



def LogoutView(request):
    logout(request)
    return redirect('/')


class ProfileView(LoginRequiredMixin,View):
    login_url = 'Users:login'
    def get(self, request):
        profile = get_object_or_404(CustomeUser, mobile=request.user.mobile)
        form=EditProfileForm(instance=profile)
        return render(request,'Profile.html',{'form':form,'profile':profile})
    def post(self, request):
        profile = get_object_or_404(CustomeUser, mobile=request.user.mobile)
        form=EditProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
             form.save()
             return redirect("Users:profile")




class UserChangePassword(LoginRequiredMixin,View):
    def get(self,request):
        form = PasswrodChangeForm()
        return  render(request,"UserChangePassword.html",{'form':form})
    def post(self,request):
        form = PasswrodChangeForm()
        if form.is_valid():
             CurrentPassword=form.cleaned_data[' CurrentPassword']
             pass1 = form.cleaned_data['Password']
             pass2 = form.cleaned_data['RePassword']
             user=self.request.user
             User=CustomeUser.objects.filter(mobile=user.mobile).first()
             if User and User.check_password(CurrentPassword) :
                User.set_password(pass1)
                User.save()
                logout(request)
                return  JsonResponse({"status":"success"})
             elif(pass1!=pass2):
                 return  JsonResponse({"status":"NotMatch"})
             else:
                     return JsonResponse({"status":"error"})

        return  render(request,'UserChangePassword.html')




