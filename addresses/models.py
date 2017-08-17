from django.db import models

class Address(models.Model):

    AC = 'AC'   
    AL = 'AL'   
    AP = 'AP'   
    AM = 'AM'   
    BA = 'BA'   
    CE = 'CE'   
    DF = 'DF'   
    ES = 'ES'   
    GO = 'GO'   
    MA = 'MA'   
    MT = 'MT'   
    MS = 'MS'   
    MG = 'MG'   
    PA = 'PA'   
    PB = 'PB'   
    PR = 'PR'   
    PE = 'PE'   
    PI = 'PI'   
    RJ = 'RJ'   
    RN = 'RN'   
    RS = 'RS'   
    RO = 'RO'   
    RR = 'RR'   
    SC = 'SC'   
    SP = 'SP'   
    SE = 'SE'   
    TO = 'TO'

    STATES_LIST=(
        (AC, 'Acre'),
        (AL, 'Alagoas'),
        (AP, 'Amapá'),
        (AM, 'Amazonas'),
        (BA, 'Bahia'),
        (CE, 'Ceará'),
        (DF, 'Distrito Federal'),
        (ES, 'Espírito Santo'),
        (GO, 'Goiás'),
        (MA, 'Maranhão'),
        (MT, 'Mato Grosso'),
        (MS, 'Mato Grosso do Sul'),
        (MG, 'Minas Gerais'),
        (PA, 'Pará'),
        (PB, 'Paraíba'),
        (PR, 'Paraná'),
        (PE, 'Pernambuco'),
        (PI, 'Piauí'),
        (RJ, 'Rio de Janeiro'),
        (RN, 'Rio Grande do Norte'),
        (RS, 'Rio Grande do Sul'),
        (RO, 'Rondônia'),
        (RR, 'Roraima '),
        (SC, 'Santa Catarina'),
        (SP, 'São Paulo'),
        (SE, 'Sergipe'),
        (TO, 'Tocantins') 

    )

    zipcode = models.CharField('CEP', max_length=9)
    street = models.CharField('Rua', max_length=200)
    number = models.CharField('Número', max_length=30)
    neighborhood = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado',choices=STATES_LIST, default=CE, max_length=2)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['city']