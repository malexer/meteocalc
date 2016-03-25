"""Module for calculation of Heat Index.

Heat Index or humiture or "feels like temperature" is an index thatcombines
air temperature and relative humidity in an attempt to determine the
human-perceived equivalent temperature.

Check wikipedia for more info:
    https://en.wikipedia.org/wiki/Heat_index
"""

import math

from temperature import Temp, F


def heat_index(temperature, humidity):
    """Calculate Heat Index based on NOAA equation.

    :param temperature: temperature value in Fahrenheit or Temp instance.
    :type temperature: int, float, Temp
    :param humidity: relative humidity in % (1-100)
    :type humidity: int, float
    :returns: Heat Index value (temperature)
    :rtype: Temp
    """

    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -6.83783e-3
    c6 = -5.481717e-2
    c7 = 1.22874e-3
    c8 = 8.5282e-4
    c9 = -1.99e-6

    T = temperature.f if isinstance(temperature, Temp) else temperature
    R = humidity

    HI = math.fsum([
        c1,
        c2 * T,
        c3 * R,
        c4 * T * R,
        c5 * T**2,
        c6 * R**2,
        c7 * T**2 * R,
        c8 * T * R**2,
        c9 * T**2 * R**2,
    ])

    return Temp(HI, units=F)
