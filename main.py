import string
import time

alfabeto = list( ' ' + string.ascii_letters)
mensagem = 'Hello World'
acumulador = ''

n = 0

while acumulador != mensagem:
    for letra in alfabeto:
        print(acumulador + letra)
        time.sleep(0.03)
        if letra == mensagem[n]:
            acumulador += letra
            n += 1
            break


print(acumulador)