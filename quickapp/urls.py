
from django.contrib import admin
from django.urls import path
from quickapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.home),
    path('gallery/', views.gallery),
]
