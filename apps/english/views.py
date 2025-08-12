from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache

@login_required
def english_main(request):
    return render(request, 'english_main.html')

@login_required
def friends0101(request):
    return render(request, 'english/friends0101/friends-01-01.html')

@login_required
def friends0102(request):
    return render(request, 'english/friends0101/friends-01-02.html')

@login_required
def friends0103(request):
    return render(request, 'english/friends0101/friends-01-03.html')

@login_required
def friends0104(request):
    return render(request, 'english/friends0101/friends-01-04.html')

@login_required
def friends0105(request):
    return render(request, 'english/friends0101/friends-01-05.html')

@login_required
def friends0106(request):
    return render(request, 'english/friends0101/friends-01-06.html')

@login_required
def friends0107(request):
    return render(request, 'english/friends0101/friends-01-07.html')

@login_required
def friends0108(request):
    return render(request, 'english/friends0101/friends-01-08.html')

@login_required
def friends0109(request):
    return render(request, 'english/friends0101/friends-01-09.html')
