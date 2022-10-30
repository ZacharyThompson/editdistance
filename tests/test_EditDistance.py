import unittest
from EditDistance import EditDist


class TestStringMethods(unittest.TestCase):

    def test_optional_optical(self):
        my_editdist = EditDist("optional", "optical")
        my_editdist.calculate()
        self.assertEqual(my_editdist.get_editdistance(), 2)

    def test_flavor_saver(self):
        my_editdist = EditDist("flavor", "saver")
        my_editdist.calculate()
        self.assertEqual(my_editdist.get_editdistance(), 3)

    def test_TGCATA_ATCTGAT(self):
        my_editdist = EditDist("TGCATA", "ATCTGAT")
        my_editdist.calculate()
        self.assertEqual(my_editdist.get_editdistance(), 5)


if __name__ == '__main__':
    unittest.main()
