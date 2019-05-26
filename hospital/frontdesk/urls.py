from django.urls import path

from . import views

app_name = 'frontdesk'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.doctorDetails, name='doctorDetails'),
    path('<int:id>/busy', views.doctorBusy, name='doctorBusy')
]