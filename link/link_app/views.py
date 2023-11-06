from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from link_app.models import Usuario, Perfil, Projeto, Demanda, Doacao, Relatorio
from django.contrib.auth.backends import BaseBackend
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Usuario, TipoDoUsuario, Projeto, Doacao, Demanda, Relatorio


def home(request):
    if request.user.is_authenticated:
        return redirect('homeLogado')
        
    context = {'home': True}
    return render(request, 'app/index.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homeLogado')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            Usuario.nomeUsuario = form.cleaned_data.get('nomeUsuario')
            Usuario.senha = form.cleaned_data.get('senha')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                    cadastro.objects.create(user=Usuario)
                    form = AuthenticationForm()
            
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('homeLogado')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #salvar os atributos e fazer  suas respectivas validacoes
            Usuario.nomeUsuario = form.save('nome de usuario')
            Usuario.senha = form.save('senha')
            Usuario.CPF = form.save('CPF')
            Usuario.CNPJ = form.save('CNPJ')
            Usuario.nascimentoData = form.save('data do nascimento')
            Usuario.cidade = form.save('cidade')
            Usuario.tipoUsuario = form.save('tipo do usuario')

            cadastro.objects.create(user=Usuario) 
            login(request, Usuario)
            return redirect('homeLogado')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})



# Create your views here.
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = 'Account was created successfully! Now Log In using your details.'


#CRIAR VALIDAÇÕES:
#CPF, CNPJ OK
# email OK
# nome de usuário, sem caracteres especiais OK
# DATA NASCIMENTO
# CIDADE



#LÓGICA:
# - VisualizarDados
# - ArmazenamentoDados 
# - AdmissãoGestor
# - RelatarAtvProj
# - CadastroDono
# - EditInfoDono
# - FiltroLoc
# - AtribResp
# - DivulgInfo