import threading

class MinhaThread(threading.Thread):
    def run(self):
        # Coloque um breakpoint nesta linha
        print("Executando a thread:", self.name)

t1 = MinhaThread()
t2 = MinhaThread()

t1.start()
t2.start()

# Coloque um breakpoint na próxima linha
print("Quantidade de threads:", threading.active_count())
