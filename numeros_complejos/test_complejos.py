import unittest
import complejos
import math

class TestComplejos(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(complejos.suma((1, 2), (3, 4)), (4, 6))
        self.assertEqual(complejos.suma((-1, 5), (1, -5)), (0, 0))
    def test_resta(self):
        self.assertEqual(complejos.resta((5, 5), (2, 3)), (3, 2))
        self.assertEqual(complejos.resta((0, 0), (1, 1)), (-1, -1))
    def test_producto(self):
        self.assertEqual(complejos.producto((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(complejos.producto((0, 1), (0, 1)), (-1, 0))
    def test_division(self):
        self.assertAlmostEqual(complejos.division((1, 2), (1, -1))[0], -0.5)
        self.assertAlmostEqual(complejos.division((1, 2), (1, -1))[1], 1.5)


    def test_conjugado(self):
        self.assertEqual(complejos.conjugado((3, -4)), (3, 4))
        self.assertEqual(complejos.conjugado((0, 5)), (0, -5))
    def test_modulo(self):
        self.assertEqual(complejos.modulo((3, 4)), 5)
        self.assertEqual(complejos.modulo((0, 0)), 0)
    def test_cartesiano_a_polar(self):
        r, theta = complejos.cartesiano_a_polar((3, 4))
        self.assertAlmostEqual(r, 5)
        self.assertAlmostEqual(theta, math.atan2(4, 3))
    def test_polar_a_cartesiano(self):
        x, y = complejos.polar_a_cartesiano((5, math.atan2(4, 3)))
        self.assertAlmostEqual(x, 3)
        self.assertAlmostEqual(y, 4)
    def test_fase(self):
        self.assertAlmostEqual(complejos.fase((1, 1)), math.pi / 4)
        self.assertAlmostEqual(complejos.fase((0, 1)), math.pi / 2)

if __name__ == "__main__":
    unittest.main()

