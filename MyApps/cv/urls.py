from django.urls import path

from . import views
# weather appname and urls
app_name='cv'
urlpatterns = [
    path('', views.index, name='index'),
    path('newCV/', views.newCV, name='newCV'),
    path('viewCVs/', views.viewCVs, name='viewCVs'),
    path('newCV/addCV/', views.addCV, name='addCV'),
    path('viewCVs/deleteCV/<int:cv_id>/', views.deleteCV, name='deleteCV'),
    path('viewCVs/printCV/<int:cv_id>/', views.printCV, name='printCV'),
]