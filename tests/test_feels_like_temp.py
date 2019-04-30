import unittest

from tests.context import feels_like, Temp


feels_like_table = {
    # Wind Chill
    # (F, Relative_Humidity, Wind_Speed_MPH): F
    (-45, 50, 5): -63,
    (-45, 50, 35): -89,
    (-45, 50, 60): -98,
    (-30, 50, 5): -46,
    (-30, 50, 35): -69,
    (-30, 50, 60): -76,
    (-15, 50, 35): -48,
    (-15, 50, 60): -55,
    (0, 50, 5): -11,
    (0, 50, 30): -26,
    (0, 50, 60): -33,
    (15, 50, 5): 7,
    (15, 50, 25): -4,
    (15, 50, 40): -8,
    (15, 50, 60): -11,
    (40, 50, 5): 36,
    (40, 50, 30): 28,
    (40, 50, 60): 25,

    # Just Temperature (no Wind Chill or Heat Index effect)
    (-45, 50, 0): -45,
    (-15, 50, 0): -15,
    (0, 50, 0): 0,
    (40, 50, 0): 40,
    (51, 50, 0): 51,
    (50, 50, 3): 50,
    (51, 50, 5): 51,
    (51, 50, 50): 51,
    (60, 50, 50): 60,
    (60, 50, 0): 60,
    (70, 50, 50): 70,
    (79, 50, 50): 79,

    # Heat Index
    # (F, Relative_Humidity, Wind_Speed_MPH): F
    (80, 40, 20): 80,
    (88, 40, 20): 88,
    (90, 40, 20): 91,
    (96, 40, 20): 101,
    (98, 40, 20): 105,
    (106, 40, 20): 124,
    (108, 40, 20): 130,
    (110, 40, 20): 136,
    (80, 65, 20): 82,
    (84, 65, 20): 89,
    (86, 65, 20): 93,
    (96, 65, 20): 121,
    (100, 65, 20): 136,
    (80, 100, 20): 87,
    (82, 100, 20): 95,
    (86, 100, 20): 112,
    (90, 100, 20): 132,
}


class FeelsLikeTest(unittest.TestCase):

    def test_feels_like_by_table(self):
        for temp_rh_wind, feels_like_f in feels_like_table.items():
            temp_f, rel_humidity, wind_speed = temp_rh_wind
            self.assertEqual(
                round(feels_like(temp_f, rel_humidity, wind_speed)),
                feels_like_f)

    def test_return_type(self):
        self.assertIsInstance(feels_like(90, 50, 5), Temp)
        self.assertIsInstance(feels_like(-45, 50, 60), Temp)
        self.assertIsInstance(feels_like(70, 50, 60), Temp)

    def test_input_temp_class(self):
        wc = feels_like(Temp(-15, unit='c'), 50, 10)
        self.assertIsInstance(wc, Temp)
        self.assertEqual(round(wc.c), -23)


if __name__ == '__main__':
    unittest.main()
