from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

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

# class RegisterView(CreateView):
#     form_class = RegisterForm
#     model = CustomeUser
#     template_name = 'Home.html'
#     success_url = "/users/profile"
#
#     def form_valid(self, form):
#         user = form.save(commit=False)
#         user.set_password(user.password)
#         user.save()
#         if self.request.is_ajax():
#             return  JsonResponse({'response':'success'})
#         return super().form_valid(form)

def RegisterView(request):
    Register=RegisterForm()
    if request.method == 'POST':
        Register=RegisterForm(request.POST)
        if  Register.is_valid():
            password =  Register.cleaned_data['Password']
            user = CustomeUser.objects.filter(mobile= Register.cleaned_data['mobile']).first()
            if user is  None:
                return  JsonResponse({'reponse':'found'})
            else:
                user1 = Register.save(commit=False)
                user1.set_password(password)
                user1.save()
            return redirect('Users:login')

    return render(request,"Home.html",{' Register': Register})



def LogoutView(request):
    logout(request)
    return redirect('Users:login')


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







