meteocalc
=========

.. image:: https://travis-ci.org/malexer/meteocalc.svg?branch=master
    :target: https://travis-ci.org/malexer/meteocalc

Several functions for calculation of meteorological variables.

Calculations were implemented based on publicly available formulas.

Implemented calculations:

1. **Dew Point** is the temperature at which dew forms.
2. **Heat Index** or "feels like temperature" is an index that combines air
   temperature and relative humidity in an attempt to determine the
   human-perceived equivalent temperature.

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

.. code-block:: python

    from meteocalc import Temp, dew_point, heat_index

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
