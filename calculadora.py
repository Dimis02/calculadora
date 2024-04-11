'''
Desenvolva uma aplicação python que simule uma calculadora onde deve solicitar para o usuario dois numeros
e a operação a ser realizada (+ - * /) conforme a operação informada deve realizar o devido calculo
e exibir para o ususario o resultado utilize match case.
'''

n1 =float (input('Informe o primeiro número: '))
o = input('Informe a operação que desejar: (+-*/)')
n2 =float (input('Informe o segundo número:'))

match o: 

    case"-":
        print("O resultado é:", n1-n2)
    case"+":
        print("O resultado é:", n1+n2)
    case"*":
        print("O resultado é:", n1*n2)
    case"/":
        print("O resultado é:", n1/n2)