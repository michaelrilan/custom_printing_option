from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
      if request.method == 'POST':
            printer= request.POST.get('printer')
            print(str(printer))
      context = {}
      
      return render(request, 'index.html',context)