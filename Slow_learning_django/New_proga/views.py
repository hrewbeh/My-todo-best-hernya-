from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo

my_mud = {'task1': 'qwerty', 'task2': 'qwerty2'}

def some(request):
	todos = Todo.objects.all()
	print(todos)
	return render(request, 'index.html', {'todos': todos})
