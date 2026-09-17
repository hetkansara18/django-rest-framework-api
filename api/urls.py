from django.urls import path
from . import views

urlpatterns = [
    #Function-Based URL
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    #Class-Based URL
    path('employees/', views.EmployeesView.as_view()),
    path('employees/<int:pk>/', views.EmployeesDetailView.as_view()),
]