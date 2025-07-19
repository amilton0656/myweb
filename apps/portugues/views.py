from django.shortcuts import render

def portugues_main(request):
    return render(request, 'portugues_main.html')

def tapas01(request):
    return render(request, 'tapas01.html')

def tapas02(request):
    return render(request, 'tapas02.html')
