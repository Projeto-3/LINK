from django.db import models

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=50, null=False, blank=False) 
    email = models.EmailField()
    cpf = models.CharField(max_length=11, null=False, primary_key=True)
    cidade = models.CharField(max_length=50, null=False)
    nascimentoData = models.DateField(max_length=10, null=False, blank=False)
    # Como criar os tipos de usuário utilizando "enum"

class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=100, null=False, blank=False)
    responsavel = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=1000, null=False, blank=False)
    contatoTelefone = models.CharField(max_length=14, null=False, blank=False)
    contatoEmail = models.EmailField()
    contatoRedeSociais = models.CharField(max_length=50, null=False, blank=False)
    demanda = models.TextField(max_length=1000, null=False, blank=False)
    idProjeto = models.CharField(primary_key=True)

class Doacao(models.Model):
    nomeDoador = models.ForeignKey(Usuario.nomeUsuario,on_delete=models.DO_NOTHING) # Ver qual é o melhor modo de deleção
    valorDoado = models.FloatField(max_length=50, null=False, blank=False)
    momentoDoacao = models.DateTimeField()
    idDoacao = models.CharField(primary_key=True)

class Demanda(models.Model):
    idProjetoD = models.ForeignKey(Projeto.idProjeto, on_delete=models.DO_NOTHING) # Ver qual é o melhor modo de deleção
    idDemanda = models.CharField(primary_key=True)
    nomeDemanda = models.CharField(max_length=50, null=False, blank=False)
    descricaoDemanda = models.TextField(max_length=200, null=False, blank=False)
    contatoDemanda = models.CharField(max_length=50, null=False, blank=False)

class Relatorio(models.Model):
    idRelatorio = models.CharField(primary_key=True)
    idProjetoR = models.ForeignKey(Projeto.idProjeto, on_delete=models.DO_NOTHING) # Ver qual é o melhor modo de deleção
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=15000, null=False, blank=False)
    dataRelatorio = models.DateTimeField()
