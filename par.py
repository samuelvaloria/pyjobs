def run():
    numero = int(input('Escribe un número: '))

    if numero%2 == 0:
        print('El número es par')
    else:
        print('El número es impar')

        print(numero)
        print(numero%2)

if __name__ == '__main__':
    run()