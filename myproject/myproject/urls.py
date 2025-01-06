from django.contrib import admin
from django.urls import include, path
from myapp import views  # Import your app's views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root path
    path('login/', views.doctor_login, name='doctor_login'),  # Login path
    path('', include('myapp.urls')),  # Include your app's URLs
]
