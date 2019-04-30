"""Module to simplify calculation of Wind chill and heat_index."""

from .temperature import Temp, F
from .windchill import wind_chill
from .heatindex import heat_index


def feels_like(temperature, humidity, wind_speed):
    """Calculate Feels Like temperature based on NOAA.

    Logic:
    * Wind Chill: temperature <= 50 F and wind > 3 mph
    * Heat Index: temperature >= 80 F
    * Temperature as is: all other cases

    Default unit for resulting Temp value is Fahrenheit and it will be used
    in case of casting to int/float. Use Temp properties to convert result to
    Celsius (Temp.c) or Kelvin (Temp.k).

    :param temperature: temperature value in Fahrenheit or Temp instance.
    :type temperature: int, float, Temp
    :param humidity: relative humidity in % (1-100)
    :type humidity: int, float
    :param wind_speed: wind speed in mph
    :type wind_speed: int, float
    :returns: Feels Like value
    :rtype: Temp

    """

    T = temperature.f if isinstance(temperature, Temp) else temperature

    if T <= 50 and wind_speed > 3:
        # Wind Chill for low temp cases (and wind)
        FEELS_LIKE = wind_chill(T, wind_speed)
    elif T >= 80:
        # Heat Index for High temp cases
        FEELS_LIKE = heat_index(T, humidity)
    else:
        FEELS_LIKE = T

    return Temp(FEELS_LIKE, unit=F)
