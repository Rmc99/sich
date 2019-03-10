from django.db import models

class Pessoa(models.Model):
    BANCO_CHOICES = (
        ("001", "001-Banco do Brasil S.A."),
        ("341", "341-Banco Itaú S.A."),
        ("033", "033-Banco Santander (Brasil) S.A."),
        ("356", "356-Banco Real S.A. (antigo)"),
        ("652", "652-Itaú Unibanco Holding S.A."),
        ("237", "237-Banco Bradesco S.A."),
        ("745", "745-Banco Citibank S.A."),
        ("399", "399-HSBC Bank Brasil S.A. – Banco Múltiplo"),
        ("104", "104-Caixa Econômica Federal"),
        ("389", "389-Banco Mercantil do Brasil S.A."),
        ("453", "453-Banco Rural S.A."),
        ("422", "422-Banco Safra S.A."),
        ("633", "633-Banco Rendimento S.A."),
    )
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome Completo")
    email = models.EmailField(max_length=150, verbose_name="E-Mail", null=True, blank=True)
    telefone = models.CharField(max_length=16, verbose_name="Telefone", help_text="Ex: 00-00000-0000", null=True, blank=True)
    cpf = models.CharField(max_length=14, null=False, verbose_name="CPF", unique=True)
    pis = models.CharField(max_length=25, null=True, blank=True, verbose_name="PIS")
    num_conta = models.CharField(max_length=30, null=False, verbose_name="Conta")
    num_agencia = models.CharField(max_length=30, null=False, verbose_name="Agência")
    num_operacao = models.CharField(max_length=30, null=True, blank=True, verbose_name="Operação")
    num_banco = models.CharField(max_length=10, null=False, choices=BANCO_CHOICES, verbose_name="Número do Banco")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Pessoa'

class Pagamento(models.Model):
    SERVIDOR_CHOICE = (
        (True, "SIM"),
        (False, "NÃO"),
    )
    MES_CHOICES = (
        (1, "Janeiro"),
        (2, "Fevereiro"),
        (3, "Março"),
        (4, "Abril"),
        (5, "Maio"),
        (6, "Junho"),
        (7, "Julho"),
        (8, "Agosto"),
        (9, "Setembro"),
        (10, "Outubro"),
        (11, "Novembro"),
        (12, "Dezembro"),
    )
    CATEGORIA_CHOICES = (
        (1, "Colaborador Interno"),
        (2, "Colaborador Externo"),
        (3, "Professor Interno"),
        (4, "Professor Externo"),
    )
    FUNCAO_CHOICES = (
        (1, "Administrativo"),
        (2, "Supervisor Orientador"),
        (3, "Coordenador"),
        (4, "Professor"),
    )
    ano = models.SmallIntegerField(null=False, verbose_name="Ano de Pagamento",help_text="Ex: 2019")
    mes = models.SmallIntegerField(null=False, choices=MES_CHOICES, verbose_name="Mês de Pagamento")
    pessoa = models.ForeignKey(Pessoa, related_name="pessoa", on_delete=models.CASCADE)
    categoria = models.SmallIntegerField(null=False, choices=CATEGORIA_CHOICES, verbose_name="Categoria")
    funcao = models.SmallIntegerField(null=False, choices=FUNCAO_CHOICES, verbose_name="Função")
    qtd_horas = models.SmallIntegerField(null=False, verbose_name="Quantidade de Horas no Mês")
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Valor da Hora")
    valor_pensao = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Pensão Alimentícia", default=0)
    valor_bruto = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Valor Bruto", default=0)
    valor_inss = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Previdencia Oficial(INSS)", default=0, help_text="Desconto de 11%")
    valor_iss = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Valor Desconto ISS", default=0, help_text="Desconto de 5%")
    qtd_dependente_irpf = models.IntegerField(null=False, verbose_name="Dependentes(quantidade)", default=0, help_text="O valor da dedução é R$ 189,59 mensais, por dependente." )
    deducao_irpf = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Total de Deduções", default=0)
    valor_pos_deducao_irpf = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Valor Pós Deduções", default=0)
    valor_irpf = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="IRPF", default=0)
    valor_liquido = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Valor Líquido", default=0)
    valor_patronal = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name="Patronal", default=0, help_text="Desconto de 20%")
    outras_deducoes = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                         verbose_name="Outras Deduções", default=0)
    dta_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    dta_atualizacao = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return str(self.ano)

    class Meta:
        verbose_name_plural = 'Pagamento'
        ordering = ['-ano', '-mes', '-categoria', '-funcao']
