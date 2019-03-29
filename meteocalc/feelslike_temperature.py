"""Module for simplify calculation of Wind chill and heat_index
"""

import math

from .temperature import Temp, F
from .windchill import wind_chill
from .heatindex import heat_index

def FeelsLikeTemperature(temperature, humidity, wind_speed):
    """Calculate Wind Chill (feels like temperature) based on NOAA.

    Default unit for resulting Temp value is Fahrenheit and it will be used
    in case of casting to int/float. Use Temp properties to convert result to
    Celsius (Temp.c) or Kelvin (Temp.k).

    :param temperature: temperature value in Fahrenheit or Temp instance.
    :type temperature: int, float, Temp
    :param humidity: relative humidity in % (1-100)
    :type humidity: int, float
    :param wind_speed: wind speed in mph
    :type wind_speed: int, float
    :returns: Wind chill value
    :rtype: Temp

    """

    T = temperature.f if isinstance(temperature, Temp) else temperature

    # Try windchil first
    if( T <= 50 and wind_speed >= 3 ):
        FEELS_LIKE = wind_chill( T, wind_speed )
    else:
        FEELS_LIKE = T

    # Replace with the Heat Index, if necessary
    if( FEELS_LIKE == T and T >= 80 ):
        FEELS_LIKE = heat_index( T, humidity )

    return Temp(FEELS_LIKE, unit=F)
