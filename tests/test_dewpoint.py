import unittest

from tests.context import dew_point, Temp

dew_point_table = {
    (-20, 76): -23,
    (-20, 52): -27,
    (-20, 20): -37,
    (-20, 9): -45,
    (-4, 90): -5,
    (-4, 52): -12,
    (-4, 32): -18,
    (-4, 11): -30,
    (0, 92): -1,
    (0, 60): -7,
    (0, 28): -16,
    (8, 93): 7,
    (8, 56): 0,
    (8, 26): -10,
    (19, 82): 16,
    (19, 39): 5,
    (19, 14): -9,
    (32, 90): 30,
    (32, 66): 25,
    (32, 35): 15,
    (32, 9): -5,
    (46, 89): 44,
    (46, 52): 34,
    (46, 22): 19,
}


class DewPointTest(unittest.TestCase):

    def test_dew_point_for_100_humidity(self):
        for t in range(-40, 60, 5):
            self.assertEqual(round(dew_point(t, 100)), t)

    def test_return_type(self):
        self.assertIsInstance(dew_point(-20, 40), Temp)

    def test_dew_point_by_table(self):
        for t_rh, dp in dew_point_table.items():
            t, rh = t_rh
            self.assertEqual(round(dew_point(t, rh)), dp)

    def test_invalid_range(self):
        self.assertRaises(ValueError, dew_point, -20, 0)
        self.assertRaises(ValueError, dew_point, -20, 100.1)


if __name__ == '__main__':
    unittest.main()
