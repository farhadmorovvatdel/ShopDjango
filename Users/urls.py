from django.urls import path
from .views import LoginView,ProfileView,RegisterView,LogoutView,UserChangePassword
app_name = 'Users'
urlpatterns = [
    path('login',LoginView,name='login'),
    path('profile',ProfileView.as_view(),name='profile'),
    path('register',RegisterView,name="register"),
    path('logout',LogoutView,name="logout"),
    path("passwordchange",UserChangePassword.as_view(),name='changepassword')

]