"""Module for calculation of Dew Point.

The dew point is the temperature at which dew forms and is a measure of
atmospheric moisture. It is the temperature to which air must be cooled
at constant pressure and water content to reach saturation.

Check wikipedia for more info:
    https://en.wikipedia.org/wiki/Dew_point
"""

import math

from .temperature import Temp, C


def dew_point(temperature, humidity):
    """Calculate Dew Point temperature.

    Two set of constants are used provided by Arden Buck: for positive and
    negative temperature ranges.

    :param temperature: temperature value in Celsius or Temp instance.
    :type temperature: int, float, Temp
    :param humidity: relative humidity in % (1-100)
    :type humidity: int, float
    :returns: Dew Point temperature
    :rtype: Temp
    """

    CONSTANTS = dict(
        positive=dict(b=17.368, c=238.88),
        negative=dict(b=17.966, c=247.15),
    )

    if humidity < 1 or humidity > 100:
        msg = 'Incorrect value for humidity: "{}". Correct range 1-100.'
        raise ValueError(msg.format(humidity))

    T = temperature.c if isinstance(temperature, Temp) else temperature
    RH = humidity

    const = CONSTANTS['positive'] if T > 0 else CONSTANTS['negative']

    pa = RH / 100. * math.exp(const['b'] * T / (const['c'] + T))

    dp = const['c'] * math.log(pa) / (const['b'] - math.log(pa))

    return Temp(dp, C)
