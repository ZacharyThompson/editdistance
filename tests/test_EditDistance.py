import unittest
from EditDistance import EditDist

class TestStringMethods(unittest.TestCase):

    def test_optional_optical(self):
        my_editdist = EditDist("optional", "optical")
        answer = my_editdist.calculateEditDistance()
        self.assertEqual(answer, 2)

    def test_flavor_saver(self):
        my_editdist = EditDist("flavor", "saver")
        answer = my_editdist.calculateEditDistance()
        self.assertEqual(answer, 3)


if __name__ == '__main__':
    unittest.main()