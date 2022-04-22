from django.db import models



class Paciente(models.Model):
    nome_paciente = models.CharField(max_length=100, null=False, blank=False)
    cpf_paciente = models.CharField(max_length=20, null=False, blank=False, unique=True)
    convenio = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    dataDeEntrada = models.DateField(null=True, blank=True)
    dataDeSaida = models.DateField(null=True, blank=True)
    
class Funcionarios(models.Model):
    nome_funcionario = models.CharField(max_length=100, null=False, blank=False)
    cpf_funcionario = models.CharField(max_length=20, null=False, blank=False)
    
    


class ConsultaAgendada(models.Model):
    data = models.DateField()
    medico = models.CharField(max_length=100, null=False, blank=False)
    especialidade_medico = models.CharField(max_length=60, null=False, blank=False)
    paciente = models.CharField(max_length=100, null=False, blank=False)
    
    