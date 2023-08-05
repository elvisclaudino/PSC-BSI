def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_primos(intervalo):
    primos = []
    for numero in range(intervalo[0], intervalo[1] + 1):
        if eh_primo(numero):
            primos.append(numero)
    print("Primos:", ", ".join(map(str, primos)))

# Exemplo de uso
intervalo = [2, 10]
imprimir_primos(intervalo)
