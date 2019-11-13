from django.shortcuts import render

def hy(request):
    return render(request, 'index.html')