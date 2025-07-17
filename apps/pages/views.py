from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def entrada(request):
	# messages.success(request, "Operação realizada com sucesso!")

	return render(request, 'registration/login.html')

def entrou(request):
    context = {}
    if request.method == 'POST':
        # Pega os dados do formulário
        username_form = request.POST.get('username')
        password_form = request.POST.get('password')

        # Autentica o usuário contra o banco de dados
        user = authenticate(request, username=username_form, password=password_form)

        if user is not None:
            # Se o usuário for válido, faz o login
            login(request, user)

            # Verifica a qual grupo o usuário pertence
            if user.groups.filter(name='english').exists():
                return redirect('english_main')
            elif user.groups.filter(name='portugues').exists():
                return redirect('portugues_main')
            else:
                # Se não pertencer a nenhum grupo, pode redirecionar para um painel padrão ou mostrar erro
                return redirect('login') # Por simplicidade, volta ao login
        else:
            # Se usuário ou senha forem inválidos
            context['error_message'] = 'Usuário ou senha inválidos.'
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)