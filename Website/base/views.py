from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
def about(request): 
    return render(request, "about.html") 
  
#def home(request): 
#    return render(request, "home.html") 
  
def savings(request): 
    return render(request, "savings.html")

def index(request): 
    return render(request, "index.html")

def debt(request): 
    return render(request, "debt.html")

def investing(request): 
    return render(request, "investing.html")

def map(request): 
    return render(request, "map.html")