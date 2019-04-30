meteocalc
=========

.. image:: https://travis-ci.org/malexer/meteocalc.svg?branch=master
    :target: https://travis-ci.org/malexer/meteocalc

Several functions for calculation of meteorological variables.

Calculations were implemented based on publicly available formulas.

Implemented calculations:

1. **Dew Point** is the temperature at which dew forms.
2. **Heat Index** is an index that combines air temperature and relative
   humidity in an attempt to determine the human-perceived equivalent
   temperature.
3. **Wind Chill** is the lowering of body temperature due to the
   passing-flow of lower-temperature air.
4. **Feels Like temperature** or Apparent temperature is the temperature
   equivalent perceived by humans, caused by the combined effects of air
   temperature, relative humidity and wind speed.

Also **Temp** class is available to convert temperature between Celsius,
Fahrenheit and Kelvin. It is also can be mixed with floats for basic math
operations.


Requirements
------------

* Python 2.7 or 3.2+


Install
-------

.. code-block:: shell

    $ pip install meteocalc


Usage
-----

..note:
    Any input Temperature value can be provided in different units:
    ``Temp(20, 'c')  # c - celsius, f - fahrenheit, k - kelvin``

.. code-block:: python

    from meteocalc import Temp, dew_point, heat_index, wind_chill, feels_like

    # create input temperature in different units
    t = Temp(20, 'c')  # c - celsius, f - fahrenheit, k - kelvin
    t2 = Temp(60, 'f')

    # calculate Dew Point
    dp = dew_point(temperature=t, humidity=56)

    # calculate Heat Index
    hi = heat_index(temperature=t2, humidity=42)

    print('Dew Point in celsius:', dp.c)
    print('Dew Point in fahrenheit:', dp.f)
    print('Heat Index in kelvin:', hi.k)

    # calculate Wind Chill
    wc = wind_chill(temperature=15, wind_speed=25)
    print('Wind Chill in fahrenheit:', wc.f)

    # calculate Feels Like temperature
    fl = feels_like(temperature=40, humidity=40, wind_speed=5)
    print('Feels Like in fahrenheit:', fl.f)


History
=======


v 1.1.0 - 2019-04-30
--------------------

Added:
~~~~~~

* Wind Chill and Feels Like temperature (thanks to @Currywurst)


v 1.0.0 - 2016-04-03
--------------------

Added:
~~~~~~

* First version

