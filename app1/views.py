from django.shortcuts import render
from django.http import HttpResponse

def fun1(request):
    return HttpResponse('<h1> app1 function1</h1>')
def fun2(request):
    return HttpResponse('<h1> app1 function2</h1>')

