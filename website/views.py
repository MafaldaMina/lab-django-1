from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def layout(request):
	return render(request, 'website/layout.html')

def ficheiro1(request):
	return render(request, 'website/ficheiro1.html')

def ficheiro2(request):
	return render(request, 'website/ficheiro2.html')

def ficheiro3(request):
	return render(request, 'website/ficheiro3.html')