from django.db import models

class Evento(models.Model):
    SITUACAO_CHOICES = (
        ("1", "Aguardando Início das Inscrições"),
        ("2", "Aberto"),
        ("3", "Encerrado"),
    )
    nome = models.CharField(max_length=200, null=False, verbose_name="Nome do Evento")
    dta_inicio = models.DateField(null=False, verbose_name="Data de Inicio do Evento")
    dta_fim = models.DateField(null=False, verbose_name="Data Final do Evento")
    situacao = models.CharField(max_length=1, null=False, choices=SITUACAO_CHOICES, verbose_name="Situação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Eventos'

class Curso(models.Model):
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome do Curso")
    qtd_vagas = models.IntegerField(null=False, verbose_name="Quantidade de Vagas")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Cursos'