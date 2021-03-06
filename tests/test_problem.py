import unittest

import theano.tensor as T

from pymanopt import Problem
from pymanopt.manifolds import Sphere


class TestProblem(unittest.TestCase):
    def setUp(self):
        self.X = X = T.vector()
        self.cost = T.exp(T.sum(X**2))

        n = self.n = 15

        self.man = Sphere(n)

    def test_prepare(self):
        problem = Problem(self.man, self.cost)
        with self.assertRaises(ValueError):
            # Asking for the gradient of a Theano cost function without
            # specifying an argument for differentiation should raise an
            # exception.
            problem.grad
