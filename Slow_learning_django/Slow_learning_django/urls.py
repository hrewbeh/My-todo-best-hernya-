from django.contrib import admin
from django.urls import path
from New_proga import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.func),
    path('qwe/', views.something)
]
