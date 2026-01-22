import time
import json
import math

class Task:
    def __init__(self, identifier, size=None):
        self.identifier = identifier
        self.size = size
        self.a = 0
        self.b = 0
        self.x = 0
        self.time = 0

    def work(self):
        start = time.time()
        time.sleep(1)
        self.time = time.time() - start
        print(f"Tâche {self.identifier} traitée en {self.time:.2f} sec")

    def to_json(self) -> str:
        """Sérialise l'objet Task en chaîne JSON."""
        data = {
            "identifier": self.identifier,
            "size": self.size,
            "a": self.a,
            "b": self.b,
            "x": self.x,
            "time": self.time,
        }
        return json.dumps(data)

    @staticmethod
    def from_json(text: str) -> "Task":
        """Désérialise une chaîne JSON en objet Task."""
        data = json.loads(text)

        task = Task(identifier=data["identifier"], size=data["size"])

        task.a = data["a"]
        task.b = data["b"]
        task.x = data["x"]
        task.time = data["time"]

        return task

    def __eq__(self, other: "Task") -> bool:
        """Définit l'égalité entre deux objets Task, en gérant la tolérance pour les floats."""
        if not isinstance(other, Task):
            return NotImplemented

        tolerance = 1e-9

        return (
            self.identifier == other.identifier
            and self.size == other.size
            and math.isclose(self.a, other.a, rel_tol=tolerance)
            and math.isclose(self.b, other.b, rel_tol=tolerance)
            and math.isclose(self.x, other.x, rel_tol=tolerance)
            and math.isclose(self.time, other.time, rel_tol=tolerance)
        )
