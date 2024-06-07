
from datetime import date

# função menu

def exibir_menu():

    meses = ('Janeiro', 'Feveriro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setrmbro', 'Outubro', 'Novembro', 'Dezembro')

    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'{dia} de {meses[mes-1]} de {ano}')

    print ('1 - calcular quadrilátero')
    print ('2 - calcular Circulo')
    print ('3 - calcular triangulo')
    print ('4 - calcular trapézio')
    print ('5 - sair do programa')

# função calcular area do quadrilátero
def calcular_quadrilateros(b,h):
    a = b * h
    return a

# função de calcular a area da circunferencia
def calcular_circunferencia (r):
    a = 3.14*r**2
    return a

# funcção para calcular a area do triangulo 
def calcular_triangulo(b,h):
    a = (b * h)/2
    return a

# função de calcular a area do trapézio
def calcular_trapezio (b_menor, b_maior, h ):
    a = ((b_menor + b_maior)*h)/ 2
    return a