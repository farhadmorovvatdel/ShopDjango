from django.urls import path
from .views import LoginView,ProfileView,RegisterView,LogoutView
app_name = 'Users'
urlpatterns = [
    path('login',LoginView,name='login'),
    path('profile',ProfileView.as_view(),name='profile'),
    path('register',RegisterView,name="register"),
    path('logout',LogoutView,name="logout"),

]