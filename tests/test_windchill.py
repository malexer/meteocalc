import unittest

from tests.context import wind_chill, Temp


# format:
# (F, MPH): F
wind_chill_table = {
    (40, 5): 36,
    (40, 30): 28,
    (40, 60): 25,
    (15, 5): 7,
    (15, 25): -4,
    (15, 40): -8,
    (15, 60): -11,
    (0, 5): -11,
    (0, 30): -26,
    (0, 60): -33,
    (-15, 35): -48,
    (-15, 60): -55,
    (-30, 5): -46,
    (-30, 35): -69,
    (-30, 60): -76,
    (-45, 5): -63,
    (-45, 35): -89,
    (-45, 60): -98,
}


class WindChillTest(unittest.TestCase):

    def test_wind_chill_by_table(self):
        for temp_wind, wind_chill_f in wind_chill_table.items():
            temp_f, wind_speed = temp_wind
            self.assertEqual(
                round(wind_chill(temp_f, wind_speed)), wind_chill_f)

    def test_return_type(self):
        self.assertIsInstance(wind_chill(40, 5), Temp)
        self.assertIsInstance(wind_chill(-45, 60), Temp)

    def test_input_temp_class(self):
        wc = wind_chill(Temp(-15, unit='c'), 10)
        self.assertIsInstance(wc, Temp)
        self.assertEqual(round(wc.c), -23)

    def test_temp50_wind4(self):
        self.assertEqual(round(wind_chill(50, 4)), 49)

    def test_temp50_wind3(self):
        self.assertRaises(ValueError, wind_chill, 50, 3)

    def test_temp51_wind3(self):
        self.assertRaises(ValueError, wind_chill, 51, 3)

    def test_temp51_wind4(self):
        self.assertRaises(ValueError, wind_chill, 51, 4)

    def test_temp100_wind60(self):
        self.assertRaises(ValueError, wind_chill, 100, 60)

    def test_temp0_wind0(self):
        self.assertRaises(ValueError, wind_chill, 0, 0)


if __name__ == '__main__':
    unittest.main()
