from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=50, null=False, blank=False) 
    email = models.EmailField()
    senha = models.CharField(max_Lenght = 30, null = False, blank = False)
    CPF = models.CharField(max_length=11, null=False, primary_key=True)
    CNPJ = models.CharField(max_length=11, null=False, primary_key=True)
    cidade = models.CharField(max_length=50, null=False)
    nascimentoData = models.DateField(max_length=10, null=False, blank=False)
    #como puxar nivel de acesso?
    tipoUsuario = models.IntegerField(max_length=1, null = False, blank=False)

    def __str__(self):
        return self.cpf
    
# Como criar os tipos de usuário utilizando "enum"
class TipoDoUsuario(Enum):
    usuarioComum = 1
    voluntario = 2
    embaixador = 3
    donoDeProjeto = 4
    Gerente = 5
    

class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=100, null=False, blank=False)
    responsavel = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=1000, null=False, blank=False)
    contatoTelefone = models.CharField(max_length=14, null=False, blank=False)
    contatoEmail = models.EmailField()
    contatoRedeSociais = models.CharField(max_length=50, null=False, blank=False)
    demanda = models.TextField(max_length=1000, null=False, blank=False)
    idProjeto = models.CharField(primary_key=True)

    def __str__(self):
        return self.idProjeto

class Doacao(models.Model):
    nomeDoador = models.ForeignKey(Usuario.nomeUsuario,on_delete=models.DO_NOTHING) # Ver qual é o melhor modo de deleção
    valorDoado = models.FloatField(max_length=50, null=False, blank=False)
    momentoDoacao = models.DateTimeField()
    idDoacao = models.CharField(primary_key=True)

    def __str__(self):
        return self.idDoacao

class Demanda(models.Model):
    idProjetoDemanda = models.ForeignKey(Projeto.idProjeto, on_delete=models.DO_NOTHING) # Ver qual é o melhor modo de deleção
    idDemanda = models.CharField(primary_key=True)
    nomeDemanda = models.CharField(max_length=50, null=False, blank=False)
    descricaoDemanda = models.TextField(max_length=200, null=False, blank=False)
    contatoDemanda = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.idProjetoDemanda
    
class Relatorio(models.Model):
    idRelatorio = models.CharField(primary_key=True)
    idProjetoRelatorio = models.ForeignKey(Projeto.idProjeto, on_delete=models.DO_NOTHING) # Ver qual é o melhor modo de deleção
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=15000, null=False, blank=False)
    dataRelatorio = models.DateTimeField()

    def __str__(self):
        return self.idProjetoRelatorio

User = get_user_model

class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "Username",
        max_length = 150,
        unique = True,
        help_text = ("Required. 150 characters or fewer. Letters, and digits only."),
        # customize the above string as you want
        validators = [username_validator],
        error_messages = {
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(max_length=254, blank=False, unique = True)
    first_name = models.CharField(max_length = 30, blank = False)
    last_name = models.CharField(max_length = 50, blank = Fals