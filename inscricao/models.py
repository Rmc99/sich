from django.db import models
from django.contrib.auth.models import User

# Classe Evento
class Evento(models.Model):
    SITUACAO_CHOICES = (
        (1, "Aguardando Início das Inscrições"),
        (2, "Aberto"),
        (3, "Encerrado"),
    )
    nome = models.CharField(max_length=200, null=False, verbose_name="Nome do Evento")
    dta_inicio = models.DateField(null=False, verbose_name="Data de Inicio do Evento")
    dta_fim = models.DateField(null=False, verbose_name="Data Final do Evento")
    situacao = models.SmallIntegerField(null=False, choices=SITUACAO_CHOICES, verbose_name="Situação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Eventos'

# Classe Curso
class Curso(models.Model):
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome do Curso")
    qtd_vagas = models.IntegerField(null=False, verbose_name="Quantidade de Vagas")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Cursos'

# Classe Candidato
class Candidato(models.Model):
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome do Candidato", blank=True)
    cpf = models.CharField(verbose_name='CPF', max_length=14, null=False, blank=True)
    endereco = models.CharField(max_length=200, null=False, verbose_name="Endereço", blank=True)
    matricula = models.CharField(max_length=25, verbose_name="Matrícula", blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, verbose_name="Sexo", blank=True)
    dta_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento", blank=True)
    curriculo = models.FileField(upload_to='uploads/', blank=True, null=True)
    celular = models.CharField(max_length=15, null=False, verbose_name="Celular", blank=True)
    usuario = models.OneToOneField(User, related_name="candidato", on_delete=models.CASCADE)

    @property
    def email(self):
        return self.usuario.email

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Candidatos'

# Classe Inscrição
class Inscricao(models.Model):
    candidato = models.ForeignKey(Candidato, related_name="inscricao", on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, related_name="evento", on_delete=models.CASCADE, blank=True)
    curso = models.ForeignKey(Curso, related_name="curso", on_delete=models.CASCADE, blank=True)
    dta_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    dta_atualizacao = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Inscrições'