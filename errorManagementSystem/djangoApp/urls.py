from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('detail/', views.machine_detail, name="machine_detail"),
    path('machine/add/', views.MachineAddView.as_view(), name="add_machine"),
    path('machine/edit/<int:pk>/', views.MachineEditView.as_view(), name='edit_machine'),
    path('overview/', views.overview_list, name='overview'),
    path('overview/<int:pk>/', views.machine_detail, name='machine_detail'),
]
