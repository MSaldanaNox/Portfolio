from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'username': 'Miguel'})

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')

def illustrations(request):
    return render(request,'illustrations.html')

def templates(request):
    return render(request,'templates.html')