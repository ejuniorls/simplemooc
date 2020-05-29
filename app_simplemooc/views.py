from django.shortcuts import render

# Create your views here.

def simplemooc(request):
    return render(request, 'simplemooc/index.html')

def contact(request):
    return render(request, 'simplemooc/contact.html')