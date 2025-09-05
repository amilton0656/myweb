from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def portugues_main(request):
    return render(request, 'portugues_main.html')

@login_required
def tapas01(request):
    return render(request, 'portugues/tapas01.html')

@login_required
def tapas02(request):
    return render(request, 'portugues/tapas02.html')

@login_required
def tapas03(request):
    return render(request, 'portugues/tapas03.html')

@login_required
def praca(request):
    return render(request, 'portugues/praca.html')

@login_required
def hangar_t6(request):
    return render(request, 'portugues/praca_aviao.html')
