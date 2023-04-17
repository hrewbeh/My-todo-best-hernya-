from django.http import HttpResponse

def func(request):
	return HttpResponse('hello')

def something(request):
	return HttpResponse('123')