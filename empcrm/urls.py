"""
URL configuration for empcrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from crm import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/add/',views.EmployeeCreateView.as_view(),name="employee-add"),
    path('employee/list/',views.EmployeeListView.as_view(),name="employee-list"),
    path('employee/<int:id>/',views.EmployeeDetailView.as_view(),name="employee-detail"),
    path('employee/<int:id>/remove/',views.EmployeeDeleteView.as_view(),name="employee-delete"),
    path('employee/<int:id>/update',views.EmployeeUpdateView.as_view(),name="employee-update"),
    path('register/',views.SignupView.as_view(),name="register"),
    path('signin/',views.SigninView.as_view(),name="signin"),
    path('signout/',views.SignoutView.as_view(),name="signout")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
