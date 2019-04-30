"""Module for calculation of Wind chill.

Wind-chill or windchill (popularly wind chill factor) is the lowering of
body temperature due to the passing-flow of lower-temperature air.

Wind chill numbers are always lower than the air temperature for values
where the formula is valid.
When the apparent temperature is higher than the air temperature,
the heat index is used instead.


Check wikipedia for more info:
    https://en.wikipedia.org/wiki/Wind_chill

Formula details:
    https://www.wpc.ncep.noaa.gov/html/windchill.shtml
"""


from .temperature import Temp, F


def wind_chill(temperature, wind_speed):
    """Calculate Wind Chill (feels like temperature) based on NOAA.

    Default unit for resulting Temp value is Fahrenheit and it will be used
    in case of casting to int/float. Use Temp properties to convert result to
    Celsius (Temp.c) or Kelvin (Temp.k).

    Wind Chill Temperature is only defined for temperatures at or below
    50 F and wind speeds above 3 mph.

    :param temperature: temperature value in Fahrenheit or Temp instance.
    :type temperature: int, float, Temp
    :param wind_speed: wind speed in mph
    :type wind_speed: int, float
    :returns: Wind chill value
    :rtype: Temp
    """

    T = temperature.f if isinstance(temperature, Temp) else temperature
    V = wind_speed

    if T > 50 or V <= 3:
        raise ValueError(
            "Wind Chill Temperature is only defined for temperatures at"
            " or below 50 F and wind speeds above 3 mph.")

    WINDCHILL = 35.74 + (0.6215 * T) - 35.75 * V**0.16 + 0.4275 * T * V**0.16

    return Temp(WINDCHILL, unit=F)
