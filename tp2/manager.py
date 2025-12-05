# tp2/manager.py
from multiprocessing.managers import BaseManager
from queue import Queue
from Task import Task  # <--- AÑADIDO: Importar la clase Task

task_queue = Queue()
result_queue = Queue()


def get_task_queue_spy():
    print("[MANAGER] -> Un client a demandé l'accès à la TASK queue")
    return task_queue


def get_result_queue_spy():
    print("[MANAGER] -> Un client a demandé l'accès à la RESULT queue")
    return result_queue


class QueueManager(BaseManager):
    pass


QueueManager.register("get_task_queue", callable=get_task_queue_spy)
QueueManager.register("get_result_queue", callable=get_result_queue_spy)
QueueManager.register("Task", Task)  # <--- AÑADIDO: Registrar Task para serialización

if __name__ == "__main__":
    # ***** MODIFICACIÓN: Usar dirección de red *****
    address = ("localhost", 50000)
    # **********************************************
    authkey = b"secret"

    # Se elimina la lógica de os.path.exists/os.remove ya que no es un socket file.

    m = QueueManager(address=address, authkey=authkey)

    print("Manager démarré... En attente.")
    s = m.get_server()
    s.serve_forever()
