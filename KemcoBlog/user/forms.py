from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Şifrenizi Giriniz", widget=forms.PasswordInput)
    

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20,label="Kullanıcı Adı")
    email = forms.EmailField(max_length=50,required=False)
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label ="Parolayı doğrula", widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Bu kullanıcı adı kullanılıyor...')
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        
        values = {
            "username" : username,
            "password" : password,
        }
        return values