from django.shortcuts import render

def index(request):
    return render(request, 'Index.html')

# Create your views here.