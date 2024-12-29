from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home_page, name='home'),
    path('machine/add/', views.MachineAddView.as_view(), name="add_machine"),
    path('machine/edit/<int:pk>/', views.MachineEditView.as_view(), name='edit_machine'),
    path('overview/<int:pk>/', views.machine_detail, name="machine_detail"),
    path('error/add/', views.ErrorAddView.as_view(), name="add_error"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('errorprotocol/', views.ProtocollView.as_view(), name="error_protocoll"),
    path('error-protocol/', views.error_protocol_details, name='error_protocol_details'),
    path('privatepolicy/', views.privatepolicy, name="policy"),
    path('machine/delete/<int:pk>/', views.delete_machine, name='delete_machine'),
    path('about/', views.about, name="about"),
]

