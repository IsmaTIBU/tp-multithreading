import unittest
from numpy.testing import assert_allclose
from task import Task


class TestTaskSolution(unittest.TestCase):
    def test_solution_accuracy(self):
        task = Task(size=552)
        task.work()
        A_x = task.a @ task.x
        assert_allclose(A_x, task.b, rtol=1e-07, atol=0.0)


if __name__ == "__main__":
    unittest.main()
