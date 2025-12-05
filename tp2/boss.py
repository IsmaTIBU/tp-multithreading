# tp2/boss.py
from client import QueueClient
from Task import Task


class Boss(QueueClient):
    def start(self):
        # 1. Enviar tareas
        for i in range(10):
            t = Task(identifier=i, size=100)
            print(f"Boss envoie la tâche {i}")
            self.task_queue.put(t)

        print("Toutes les tâches sont envoyées.")

        # 2. Recibir resultados
        for i in range(10):
            res = self.result_queue.get()
            print(f"Boss a reçu le résultat de la tâche {res.identifier}")


if __name__ == "__main__":
    boss = Boss()
    boss.start()
