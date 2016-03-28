import unittest

from tests.context import Temp


temperature_values = (
    dict(c=-273.15, f=-459.67, k=0),
    dict(c=-100, f=-148, k=173.15),
    dict(c=-30, f=-22, k=243.15),
    dict(c=-20, f=-4, k=253.15),
    dict(c=-10, f=14, k=263.15),
    dict(c=0, f=32, k=273.15),
    dict(c=10, f=50, k=283.15),
    dict(c=20, f=68, k=293.15),
    dict(c=100, f=212, k=373.15),
    dict(c=200, f=392, k=473.15),
    dict(c=300, f=572, k=573.15),
)


class TempTest(unittest.TestCase):

    def test_celcius_to_celcius(self):
        for t in temperature_values:
            temp = Temp(t['c'], unit='C')
            self.assertEqual(temp.c, t['c'])

    def test_fahrenheit_to_fahrenheit(self):
        for t in temperature_values:
            temp = Temp(t['f'], unit='F')
            self.assertEqual(temp.f, t['f'])

    def test_kelvin_to_kelvin(self):
        for t in temperature_values:
            temp = Temp(t['k'], unit='K')
            self.assertEqual(temp.k, t['k'])

    def test_celcius_to_fahrenheit(self):
        for t in temperature_values:
            temp = Temp(t['c'], unit='C')
            self.assertEqual(round(temp.f, 2), t['f'])

    def test_celcius_to_kelvin(self):
        for t in temperature_values:
            temp = Temp(t['c'], unit='C')
            self.assertEqual(round(temp.k, 2), t['k'])

    def test_fahrenheit_to_celcius(self):
        for t in temperature_values:
            temp = Temp(t['f'], unit='F')
            self.assertEqual(round(temp.c, 2), t['c'])

    def test_fahrenheit_to_kelvin(self):
        for t in temperature_values:
            temp = Temp(t['f'], unit='F')
            self.assertEqual(round(temp.k, 2), t['k'])

    def test_kelvin_to_celcius(self):
        for t in temperature_values:
            temp = Temp(t['k'], unit='K')
            self.assertEqual(round(temp.c, 2), t['c'])

    def test_kelvin_to_fahrenheit(self):
        for t in temperature_values:
            temp = Temp(t['k'], unit='K')
            self.assertEqual(round(temp.f, 2), t['f'])

    def test_add_with_float(self):
        t = Temp(243.15, unit='K')
        t2 = 40 + t
        self.assertEqual(float(t2), 283.15)
        self.assertEqual(t2.c, 10)
        self.assertEqual(t2.f, 50)
        self.assertEqual(t2.k, 283.15)
        self.assertIsInstance(t2, Temp)

    def test_sub_with_float(self):
        t = Temp(68, unit='F')
        t2 = t - 36
        self.assertEqual(int(t2), 32)
        self.assertEqual(t2.c, 0)
        self.assertEqual(t2.f, 32)
        self.assertEqual(t2.k, 273.15)
        self.assertIsInstance(t2, Temp)

    def test_mul_with_float(self):
        t = Temp(100, unit='C')
        t2 = t * 2
        self.assertEqual(int(t2), 200)
        self.assertEqual(t2.c, 200)
        self.assertEqual(t2.f, 392)
        self.assertEqual(t2.k, 473.15)
        self.assertIsInstance(t2, Temp)

    def test_truediv_with_float(self):
        t = Temp(573, unit='K')
        t2 = t / 2
        self.assertEqual(t2.k, 286.5)
        self.assertEqual(round(t2.c, 2), 13.35)
        self.assertEqual(round(t2.f, 2), 56.03)
        self.assertEqual(t2.k, 286.5)
        self.assertIsInstance(t2, Temp)

    def test_neg_with_float(self):
        t = Temp(-22, unit='F')
        t2 = -t
        self.assertEqual(int(t2), 22)
        self.assertEqual(round(t2.c, 2), -5.56)
        self.assertEqual(t2.f, 22)
        self.assertEqual(round(t2.k, 2), 267.59)
        self.assertIsInstance(t2, Temp)


if __name__ == '__main__':
    unittest.main()
