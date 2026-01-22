# tp2/manager.py
from multiprocessing.managers import BaseManager
from queue import Queue
from Task import Task

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
QueueManager.register("Task", Task)

if __name__ == "__main__":
    address = ("localhost", 50000)
    authkey = b"secret"

    m = QueueManager(address=address, authkey=authkey)

    print("Manager démarré... En attente.")
    s = m.get_server()
    s.serve_forever()
