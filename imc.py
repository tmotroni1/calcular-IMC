import os

while True:

    nome = input('Digite seu nome: ')
    peso = input('Digite seu peso: ')
    altura = input('Digite sua altura: ')

    float_peso = float(peso)
    float_altura = float(altura)
    imc = float_peso / (float_altura * float_altura)
    print(f'Seu IMC (Indice de massa corporal) é: {imc:.2f}')


    if imc <= 18.5:
        print('Abaixo do normal.')
    elif imc >= 18.6 and imc <= 24.9:
        print('Normal.')
    elif imc >= 25.0 and imc <= 29.9:
        print('Sobre peso')
    elif imc >= 30 and imc <= 34.9:
        print('Obesidade. grau I. Sinal de alerta')
    elif imc >= 35 and imc <= 39.9:
        print('Obesidade grau II.')
    else: 
        print('Obesidade Grau III')
        
    continuar = input('Deseja calcular novamente? [s]im [n]ão: ')
    if continuar == 's':
        continue
    else:
        os.system('cls') # Depending on your operating system, 'cls' may not work, if it gives an error, replace it with 'clear'
        break
        