from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeesViewset, basename='employees')

urlpatterns = [
    #Function-Based URL
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    #Class-Based URL
    #path('employees/', views.EmployeesView.as_view()),
    #path('employees/<int:pk>/', views.EmployeesDetailView.as_view()),

    path('', include(router.urls)),
]