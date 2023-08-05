import time
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

start_time = time.time()

sub_intervalos = [[100000, 200000], [200000, 300000], [300000, 400000], [400000, 500000], [500000, 600000], [600000, 700000], [700000, 800000], [800000, 900000], [900000, 1000000]]
threads = []

for intervalo in sub_intervalos:
    thread = MinhaThread(intervalo)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
end_time = time.time()
execution_time = end_time - start_time

print("Tempo de execução (exemplo com várias threads):", execution_time)