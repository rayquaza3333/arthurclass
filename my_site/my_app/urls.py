"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views

app_name = 'homework'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.HomeworkCreateView.as_view(), name='create'),
    path('update/', views.HomeworkCreateView.as_view(), name='update'),
    path('delete/', views.HomeworkDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.HomeworkDetailView.as_view(), name='detail'),
    path('', views.HomeworkListView.as_view(), name='all'),

]
