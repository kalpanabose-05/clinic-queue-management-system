from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    

    path('dashboard/', views.dashboard, name='dashboard'),
    path('insurance/', views.insurance, name='insurance'),
    path('services/', views.services, name='services'),
    path('specialities/', views.specialities, name='specialities'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('patient/', views.patient, name='patient'),
    path('admin-page/', views.admin, name='admin_page'),
    path('appointment/', views.appointment, name='appointment'),

    path('queue/', views.queue, name='queue'),
    path('queue/next/', views.next_patient, name='next_patient'),

    path('confirm/', views.confirm, name='confirm'),

    path(
        'insurance/<str:insurance_type>/',
        views.insurance_detail,
        name='insurance_detail'
    ),
    path('doctors/', views.doctors, name='doctors'),
    path('patient_history/', views.patient_history, name='patient_history'),
    

]