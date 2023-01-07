from django.contrib import admin
from django.urls import path
from notlar import views
app_name = "notlar"
urlpatterns = [
    path('addNot', views.addNot, name="addNot"),
    path('deleteNot/<int:id>', views.deleteNot, name="deleteNot"),
    path('updateNot/<int:id>', views.updateNot, name="updateNot"),
    path('detailNot/<int:id>', views.detailNot, name="detailNot"),
    path('dashboardNot', views.dashboardNot, name="dashboardNot"),
    path('', views.notlar, name="notlar"),
]