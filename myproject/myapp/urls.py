from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path("Logout",views.Logout,name="Logout"), # Home view under /translate/
    path('login/', views.doctor_login, name='doctor_login'),  # Login view under /translate/login/
    path('patient/form/', views.patient_form, name='patient_form'),
    path('patient/form/<int:patient_id>/', views.patient_form, name='edit_patient'),
    path('patient-list/', views.patient_list, name='patient_list'), 
    path('patient/view/<int:patient_id>/', views.patient_view, name='patient_view'),
    path('patient/export/', views.export_patient_data, name='export_patient_data'),
    path('patient/delete/<int:patient_id>/', views.patient_delete, name='patient_delete'),
]
