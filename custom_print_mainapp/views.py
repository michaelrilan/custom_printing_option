from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import print_option_form
import win32print
import win32api
# Create your views here.

def index(request):
      form = print_option_form()
      currentprinter = win32print.GetDefaultPrinter()
      if request.method == 'POST':
            printer = request.POST.get('print_name')
            doc_file = request.POST.get('doc_file')
            copies = request.POST.get('copies')
            layout = request.POST.get('layout')
            colored = request.POST.get('colored')
            pages = request.POST.get('pages')




            print(str(printer))
      context = {}
      
      return render(request, 'index.html',context)