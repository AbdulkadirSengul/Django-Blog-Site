from django.contrib import admin
from django.urls import path
from projeler import views
app_name = "projeler"
urlpatterns = [
    path('addProje', views.addProje, name="addProje"),
    path('deleteProje/<int:id>', views.deleteProje, name="deleteProje"),
    path('updateProje/<int:id>', views.updateProje, name="updateProje"),
    path('detailProje/<int:id>', views.detailProje, name="detailProje"),
    path('dashboardProje', views.dashboardProje, name="dashboardProje"),
    path('', views.projeler, name="projeler"),
]