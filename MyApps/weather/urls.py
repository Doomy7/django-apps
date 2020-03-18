from django.urls import path

from . import views
# weather appname and urls
app_name='weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addCity, name='addCity'),
    path('delete/<int:city_id>', views.deleteCity, name='delCity'),
]