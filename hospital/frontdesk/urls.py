from django.urls import path

from . import views

app_name = 'frontdesk'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:doctor_name>/', views.doctorDetails, name='doctorDetails'),
    path('<str:doctor_name>/busy', views.doctorBusy, name='doctorBusy')
]