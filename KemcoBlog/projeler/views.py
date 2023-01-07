from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProjeForm
from .models import Proje
from django.contrib import messages

# Create your views here.
def projeler (request): 
    projelerr = Proje.objects.all()
    context = {
        "projelerr":projelerr
    } 
    return render(request,'projeler.html',context)

def addProje(request):
    form = ProjeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        projeler = form.save(commit=False)
        projeler.author_prj = request.user
        projeler.save()
        messages.success(request,"Proje Başarı ile oluşturuldu")
        return redirect("home")
    return render(request,'addProje.html',{"form":form})

def dashboardProje(request):
    projeler = Proje.objects.filter(author_prj = request.user)
    context = {
        "projeler":projeler
    }
    return render(request,'dashboardProje.html',context)

def deleteProje(request,id):
    projeler = get_object_or_404(Proje,id=id)
    projeler.delete()
    messages.success(request,"Başarı ile silinmiştir..")
    return redirect("projeler:dashboardProje")

def updateProje(request,id):
    projeler = get_object_or_404(Proje,id=id)
    form = ProjeForm(request.POST or None, request.FILES or None,instance=projeler)
    if form.is_valid():
        projeler = form.save(commit=False)
        projeler.author_prj = request.user
        projeler.save()
        messages.success(request,"Proje Başarı ile güncellendi")
        return redirect("projeler:dashboardProje")
    return render(request,'addProje.html',{"form":form})
    

def detailProje(request,id):
    projeler = get_object_or_404(Proje,id=id)
    return render(request,'detailProje.html',{"projeler":projeler})


