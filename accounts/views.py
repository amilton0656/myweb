from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login
from django.contrib import messages

@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # vem do {{ form.username }}
        password = request.POST.get('password')  # vem do {{ form.password }}

        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)

            # fallback (sem grupo)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')  # seu template acima

# Página protegida - só acessa logado
@login_required
@never_cache
def home(request):
    grupos = list(request.user.groups.values_list("name", flat=True))
    print(grupos)

    # if request.user.groups.filter(name='portugues').exists():
    #     return render(request, 'home_portugues.html')
    # elif request.user.groups.filter(name='english').exists():
    #     return render(request, 'home_english.html')
    # else:
    return render(request, 'home.html')

@login_required
@never_cache
def home_portugues(request):
    return render(request, 'home_portugues.html')

@login_required
@never_cache
def home_english(request):
    return render(request, 'home_english.html')

@login_required
@never_cache
def geral(request):
    return render(request, "geral.html")

# Logout forçado - limpa sessão e redireciona pro login
@never_cache
def do_logout(request):
    logout(request)
    request.session.flush()
    return redirect("login")
