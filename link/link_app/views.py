from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from link_app.models import Usuario, Perfil, Projeto, Demanda, Doacao, Relatorio

def home(request):
    if request.user.is_authenticated:
        return redirect('') #Ve para onde redirecionar (MarketPlace)
        
    context = {'home': True}
    return render(request, 'app/index.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('') #home
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            senha = form.cleaned_data.get('senha')
            user = authenticate(email=email, senha=senha)
            if user is not None: 
                login(request, user)
                return redirect('') #home
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})


def cadastro(request): 
    if request.mathot == 'GET':
        return render(request, ) #template
    else: 
        email == request.POST.get('email')
        senha == request.POST.get('senha')
        nomeUsuario == request.POST.get('nomeUsuario')
        user = Usuario.object.filter(email = email).first()
        #Verificar os outros atributos, especial o CPF válido ou não 
    # cpf 
    # cidade 
    # nascimentoData 
    # tipoUsuario


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

def Visualizacao(request):