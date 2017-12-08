import unittest, math
from inlay_module.date_used import average


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20,30,70]), 40.0)

unittest.main()

