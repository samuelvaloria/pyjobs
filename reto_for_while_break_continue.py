def run():
    contador = 0
    while contador < 56:
        contador = contador + 1
        print(contador)

def run2():
    for i in range(100):
        print('2 por ' + str(i) + ' es: ' + str(2 * i))

def run3():
    nombre = input('Escribe tu nombre, máquina!: ')
    for letra in nombre:
        print(letra.lower())

def run4():
    nombre2 = input('Escribe la mejor frase que se te ocurra: ')
    for letra2 in nombre2:
        if letra2 == 'i':
            break
        print(letra2)


if __name__ == '__main__':
    run()

if __name__ == '__main__':
    run2()

if __name__ == '__main__':
    run3()

if __name__ == '__main__':
    run4()