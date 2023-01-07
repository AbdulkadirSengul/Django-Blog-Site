from django.shortcuts import render,redirect,get_object_or_404
from .forms import NotlarForm
from .models import Notlar
from django.contrib import messages
# Create your views here.
def home (request):
    return render(request,'home.html')

def addNot(request):
    form = NotlarForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        notlar = form.save(commit=False)
        notlar.author_nt = request.user
        notlar.save()
        messages.success(request, "Başarı ile eklendi")
        return redirect("home")
    return render(request,"addNot.html",{"form":form})
def deleteNot(request,id):
    notlar = get_object_or_404(Notlar,id=id)
    notlar.delete()
    messages.success(request,"Başarı ile silindi")
    return redirect("notlar:dashboardNot")
def updateNot(request,id):
    notlar = get_object_or_404(Notlar,id=id)
    form = NotlarForm(request.POST or None, request.FILES or None, instance=notlar)
    if form.is_valid():
        notlar = form.save(commit=False)
        notlar.author_nt = request.user
        notlar.save()
        messages.success(request, "Başarı ile güncellendi")
        return redirect("home")
    return render(request,"addNot.html",{"form":form})
def detailNot(request,id):
    notlar = get_object_or_404(Notlar,id=id)
    return render(request,"detailNot.html",{"notlar":notlar})
def dashboardNot(request):
    notlar = Notlar.objects.filter(author_nt = request.user)
    context = {
        "notlar":notlar
    }
    return render (request,'dashboardNot.html',context)
def notlar (request):
    notlarr = Notlar.objects.all()
    context={
        "notlarr":notlarr
    }
    return render(request,'notlar.html',context)
