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

            # Decide para onde enviar conforme o grupo
            if user.groups.filter(name='portugues').exists():
                return redirect('portugues_main')  # crie essa URL
            if user.groups.filter(name='english').exists():
                return redirect('english_main')    # crie essa URL

            # fallback (sem grupo)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')  # seu template acima

# Página protegida - só acessa logado
@login_required
@never_cache
def home(request):
    user = request.user
    if user.groups.filter(name='portugues').exists():
        return render(request, 'portugues_main.html')
    if user.groups.filter(name='english').exists():
        return render(request, 'english_main.html')
    return render(request, 'home.html')  # fallback

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
