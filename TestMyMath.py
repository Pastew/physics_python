import unittest

from MyMath import Wektor


class TestMyMath(unittest.TestCase):

    def test_multiply_vector_with_number(self):
        v = Wektor(1.0, 0.0, 0.0)
        v = v * 3.0

        self.assertEqual([v.x, v.y, v.z], [3.0, 0.0, 0.0])

    def test_multiply_number_with_vector(self):
        v = Wektor(1.0, 0.0, 0.0)
        v = 3.0 * v

        self.assertEqual([v.x, v.y, v.z], [3.0, 0.0, 0.0])

    def test_div_vector_and_number(self):
        v = Wektor(3.0, 0.0, 0.0)
        v = v / 3.0

        self.assertTrue(isinstance(v,Wektor))
        self.assertEqual([v.x, v.y, v.z], [1.0, 0.0, 0.0])

    def test_multiply_vector_with_vector(self):
        v1 = Wektor(2.0, -1.0, 1.0)
        v2 = Wektor(3.0, 4.0, 5.0)
        expected = 7.0  # 2*3 -4 +5 = 7
        self.assertEqual(v1*v2, expected)

    def test_sub_vector_with_vector(self):
        v1 = Wektor(2.0, -1.0, 1.0)
        v2 = Wektor(3.0, 4.0, 5.0)
        expected = [-1.0, -5.0, -4.0]
        result = (v1 - v2)
        self.assertEqual([result.x, result.y, result.z], expected)

if __name__ == '__main__':
    unittest.main()
