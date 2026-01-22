import unittest
from .Task import Task


class TestTaskSerialization(unittest.TestCase):
    def setUp(self):
        """Configure une tâche avec des valeurs distinctes pour le test."""
        self.task_a = Task(identifier=42, size=500)
        self.task_a.a = 3.14159265
        self.task_a.b = 2.71828
        self.task_a.x = 1.0
        self.task_a.time = 0.001234567

    def test_serialization_and_equality(self):
        a = self.task_a
        txt = a.to_json()
        b = Task.from_json(txt)
        self.assertEqual(
            a, b, "L'objet désérialisé (b) doit être égal à l'objet original (a)."
        )
        self.assertIsNot(a, b)


if __name__ == "__main__":
    unittest.main()
