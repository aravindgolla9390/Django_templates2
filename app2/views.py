from django.shortcuts import render

def htmlfile1(request):
    return render(request,'htmlfile1.html')
def htmlfile2(request):
    return render(request,'htmlfile2')
