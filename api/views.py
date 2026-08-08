from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentsView(request):
    students = [
    {'id': 1, 'name': 'Raj', 'class': 'Python/Django Developer'},
    {'id': 2, 'name': 'Het', 'class': 'Python/Django Developer'}
    ]
    return JsonResponse(students, safe=False)