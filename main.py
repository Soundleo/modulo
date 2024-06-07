# importa o modulo
import os
from modulo import * 

# programa principal
if __name__ == '__main__':
    while True:
        print (f'{exibir_menu()}')
        opcao = input('informe a opção desejada: ')
        os.system('cls')
        
        
        match opcao:
            case '1':
                 #quadrilátero
                b = int(input('Base do quadrilátero: '))
                h = int(input('Altura do quadrilátero: '))
                print(f'Área do quadriátero é: {calcular_quadrilateros(b,h)}')
                continue
            case '2': 
                #circulo
                r = int(input('Qual o raio do circulo: '))
                print(f'Área da circuferência é: {calcular_circunferencia}')
                continue
            case '3':
                #triângulo
                b = int(input('Base do triângulo: '))
                h = int(input('Altura do triângulo: '))
                print(f'Área da triângulo é: {calcular_triangulo}')
                continue
            case '4':
                #trapézio
                b_menor = int(input('Informa a base menor do trapézio: '))
                b_maior = int(input('Informa a base maior do trapézio: '))
                print(f'Área do trapézio é: {calcular_trapezio}')
                continue

            case _ :
                break