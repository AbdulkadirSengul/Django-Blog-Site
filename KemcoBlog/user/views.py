from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
# Create your views here.
@csrf_exempt
def loginuser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        userr = authenticate(username = username, password = password)
        if userr is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı...")
            return render(request,"login.html",context)
        messages.success(request,"Başarı ile giriş yapıldı")
        login(request,userr)
        return redirect("home")
    return render(request, 'login.html',context)
def logoutuser(request):
    logout(request)
    messages.success(request,"Başarı ile çıkış yapıldı")
    return redirect("home")

@csrf_exempt
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarı ile kayıt olundu")
        return redirect("home")
    context = {
        "form":form
    }
    return render(request, 'register.html',context)