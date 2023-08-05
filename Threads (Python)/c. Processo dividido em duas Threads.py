import threading

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
    print(f"Primos no intervalo {intervalo}:", ", ".join(map(str, primos)))

class MinhaThread(threading.Thread):
    def __init__(self, intervalo):
        super().__init__()
        self.intervalo = intervalo

    def run(self):
        imprimir_primos(self.intervalo)

intervalo = [2, 10]
metade = (intervalo[1] - intervalo[0]) // 2

t1 = MinhaThread([intervalo[0], intervalo[0] + metade])
t2 = MinhaThread([intervalo[0] + metade + 1, intervalo[1]])

t1.start()
t2.start()

t1.join()
t2.join()

print("Concluído.")
