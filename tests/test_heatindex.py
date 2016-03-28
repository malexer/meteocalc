import unittest

from tests.context import heat_index, Temp


heat_index_noaa_table = {
    (80, 40): 80,
    (88, 40): 88,
    (90, 40): 91,
    (96, 40): 101,
    (98, 40): 105,
    (106, 40): 124,
    (108, 40): 130,
    (110, 40): 136,
    (80, 65): 82,
    (84, 65): 89,
    (86, 65): 93,
    (96, 65): 121,
    (100, 65): 136,
    (80, 100): 87,
    (82, 100): 95,
    (86, 100): 112,
    (90, 100): 132,
}


class HeatIndexTest(unittest.TestCase):

    def test_heat_index_by_noaa_table(self):
        for t_rh, hi in heat_index_noaa_table.items():
            t, rh = t_rh
            self.assertEqual(round(heat_index(t, rh)), hi)

    def test_return_type(self):
        self.assertIsInstance(heat_index(80, 40), Temp)
        self.assertIsInstance(heat_index(52, 56), Temp)

    def test_input_temp_class(self):
        hi = heat_index(Temp(30, units='c'), 70)
        self.assertIsInstance(hi, Temp)
        self.assertEqual(round(hi.c), 35)
        self.assertEqual(round(hi, 1), 95.1)


if __name__ == '__main__':
    unittest.main()
