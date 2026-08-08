from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
        {'id':1, 'name':'Raj', 'age':31},
        {'id':2, 'name':'Het', 'age':25}
    ]
    return HttpResponse(students)