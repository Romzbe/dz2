from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reqest):
    return render(reqest, 'main/index.html')

def too(reqest):
    return render(reqest, 'main/too.html')
def tre(reqest):
    return render(reqest, 'main/tre.html')
def defold(reqest):
    return render(reqest, 'main/defold.html')

def about(reqest):
    return HttpResponse('<h1>Про нас</h1>')
