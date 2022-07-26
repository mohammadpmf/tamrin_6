from django.shortcuts import render
from .models import Student

def show_info(request):
    context = { 'students' : Student.objects.all()}
    return render(request, 'info/index.html', context)