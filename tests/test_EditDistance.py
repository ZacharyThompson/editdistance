import unittest
from EditDistance import EditDist

class TestStringMethods(unittest.TestCase):

    def test_optional_optical(self):
        my_editdist = EditDist("optional", "optical")
        my_editdist.calculate()
        self.assertEqual(my_editdist.getEditDistance(), 2)

    def test_flavor_saver(self):
        my_editdist = EditDist("flavor", "saver")
        my_editdist.calculate()
        self.assertEqual(my_editdist.getEditDistance(), 3)

    def test_TGCATA_ATCTGAT(self):
        my_editdist = EditDist("TGCATA", "ATCTGAT")
        my_editdist.calculate()
        self.assertEqual(my_editdist.getEditDistance(), 5)
        self.assertEqual(my_editdist._similarityMatrix[7][6], 4)
        my_editdist.printAlignment()


if __name__ == '__main__':
    unittest.main()