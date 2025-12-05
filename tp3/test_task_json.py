import unittest

# CORRECTION: Utiliser l'importation relative pour trouver Task.py dans le même répertoire
from .Task import Task


class TestTaskSerialization(unittest.TestCase):
    def setUp(self):
        """Configure une tâche avec des valeurs distinctes pour le test."""
        self.task_a = Task(identifier=42, size=500)
        self.task_a.a = 3.14159265
        self.task_a.b = 2.71828
        self.task_a.x = 1.0
        self.task_a.time = 0.001234567  # Valeur float pour tester __eq__

    # TP 3 - Étape 4: Tester l'égalité
    def test_serialization_and_equality(self):
        """
        Teste la sérialisation (a -> txt), la désérialisation (txt -> b),
        et s'assure que a == b.
        """
        # 1. Instancier la première Task (Déjà fait dans setUp)
        a = self.task_a

        # 2. Sérialisation de la première Task
        txt = a.to_json()

        # 3. Désérialisation en une seconde Task
        b = Task.from_json(txt)

        # 4. S'assurer que a == b
        self.assertEqual(
            a, b, "L'objet désérialisé (b) doit être égal à l'objet original (a)."
        )

        # Vérification supplémentaire: Assurer qu'ils sont des objets distincts en mémoire
        self.assertIsNot(a, b)


if __name__ == "__main__":
    unittest.main()
