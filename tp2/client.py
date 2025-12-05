# tp2/client.py
from multiprocessing.managers import BaseManager
from Task import (
    Task,
)  # <--- AÑADIDO: Necesario para que el cliente reconozca la clase Task


class QueueManager(BaseManager):
    pass


QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")
QueueManager.register(
    "Task", Task
)  # <--- AÑADIDO: Registrar Task en el lado del cliente


class QueueClient:
    def __init__(self):
        # ***** MODIFICACIÓN: Usar dirección de red *****
        address = ("localhost", 50000)
        # **********************************************
        authkey = b"secret"

        print(f"Tentative de connexion sur : {address}")

        self.manager = QueueManager(address=address, authkey=authkey)
        self.manager.connect()
        self.task_queue = self.manager.get_task_queue()
        self.result_queue = self.manager.get_result_queue()
        print("Client connecté au Manager.")
