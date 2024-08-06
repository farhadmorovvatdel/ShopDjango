from  django import  forms
from .models import CustomeUser
class LoginForm(forms.Form):
    Mobile=forms.CharField(max_length=11,label="موبایل",widget=forms.TextInput(attrs={
        'class':'e-field-inner',
        'placeholder':'لطفا موبایل خود را وارد نمایید',
        'id':"LoginMobile"
    }))
    Password=forms.CharField(max_length=11,label="رمز عبور",widget=forms.PasswordInput(attrs={
        'class':'e-field-inner',
        'placeholder': 'لطفا رمز عبور خود را وارد نمایید',
        'id':'LoginPassword'
    }))
class RegisterForm(forms.ModelForm):
    Password = forms.CharField(max_length=30, required=True, label=" رمز عبور",
                                 widget=forms.PasswordInput(attrs={
                                     'class': 'e-field-inner',
                                     'placeholder': 'لطفا رمز عبور خود را وارد نمایید',
                                     'id': 'RegisterPassword'
                                 }))
    RePassword=forms.CharField(max_length=30,required=True,label="تکرار رمز عبور",widget=forms.PasswordInput(attrs={
        'class': 'e-field-inner',
        'placeholder': 'لطفا تکرار رمز عبور خود را وارد نمایید',
        'id':'RegisterRePassword'
    }))
    class Meta:


        model=CustomeUser
        fields=['mobile','Password',"RePassword"]
        error_messages = {
           'mobile':{
               'required':'این فیلد اجباری میباشد',
               'max_length':'شماره موبایل نمیتواند بیشتر از 11 کاراکتر باشد'
           },



        }
        required={
        'mobile':True,

        }
        labels = {
            'mobile':"شماره تلفن",
            'password':'رمز عبور'


        }
        widgets={
            "mobile":forms.TextInput(attrs={
                'class': 'e-field-inner',
                'placeholder': 'لطفا موبایل خود را وارد نمایید',
                'id':'RegisterMobile'
            }),
            'password':forms.PasswordInput(attrs={
                'class': 'e-field-inner',
                'placeholder': 'لطفا رمز  عبور خود را وارد نمایید',
            }),

        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomeUser
        fields = ('first_name','last_name','email','Image')
        labels={
            "first_name":"نام",
            "last_name":"نام خانوادگی",
            "email":"ایمیل",
            "Image":"تصویر کاربری"
        }
        widgets={
            "first_name":forms.TextInput(attrs={
                'class':'e-field-inner',
                 'placeholder':"نام خود را وارد نمایید"
            }),
            "last_name": forms.TextInput(attrs={
                'class': 'e-field-inner',
                'placeholder': "نام خانوادگی خود را وارد نمایید"
            }),
            "email": forms.EmailInput(attrs={
                'class': 'e-field-inner',
                'placeholder': "ایمیل خود را وارد نمایید"
            }),
        "Image": forms.FileInput(attrs={
            'id':"user_profile"
        })


        }

class PasswrodChangeForm(forms.Form):
    CurrentPassword = forms.CharField(max_length=30, required=True, label=" رمز عبور",
widget=forms.PasswordInput(attrs={
'class': 'e-field-inner',
 'placeholder': 'لطفا رمز عبور خود را وارد نمایید',
 'id': 'CurrentPassword_id'
 }))

    Password = forms.CharField(max_length=30, required=True, label=" رمز عبور",
widget=forms.PasswordInput(attrs={
'class': 'e-field-inner',
'placeholder': 'لطفا رمز عبور خود را وارد نمایید',
 'id': 'ChangePassword_id'
}))
    RePassword = forms.CharField(max_length=30, required=True, label="تکرار رمز عبور",widget=forms.PasswordInput(attrs={
'class': 'e-field-inner','placeholder': 'لطفا تکرار رمز عبور خود را وارد نمایید','id': 'ChanegRePassword_id'
                                 }))