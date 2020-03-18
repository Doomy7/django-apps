from django.urls import path

from . import views

app_name='To_Do_stickers'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('add/', views.add, name='add'),
]