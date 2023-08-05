import threading
import random
import time


class Cofre:
    def __init__(self):
        self.senha = str(random.randint(0, 99999))

    def verificar_senha(self, tentativa):
        return tentativa == self.senha


class Hackers(threading.Thread):
    def __init__(self, cofre, policia):
        super().__init__()
        self.cofre = cofre
        self.policia = policia

    def run(self):
        for i in range(100000):
            if self.cofre.verificar_senha(str(i)):
                print("Hacker", self.name, "abriu o cofre com a senha:", i)
                self.policia.interromper()
                return


class Policiais(threading.Thread):
    def __init__(self, tempo_maximo):
        super().__init__()
        self.tempo_maximo = tempo_maximo
        self.interrupcao = threading.Event()

    def interromper(self):
        self.interrupcao.set()

    def run(self):
        for i in range(self.tempo_maximo, 0, -1):
            print("Tempo restante para a polícia chegar:", i)
            time.sleep(1)
            if self.interrupcao.is_set():
                return
        print("A polícia pegou os hackers e eles estão presos.")


cofre = Cofre()

policia = Policiais(tempo_maximo=10)
policia.start()

hackers = []
for _ in range(2):
    hacker = Hackers(cofre, policia)
    hackers.append(hacker)
    hacker.start()

for hacker in hackers:
    hacker.join()

policia.join()

print("Fim da simulação.")
