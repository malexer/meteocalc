"""Temperature conversion routines."""


C = 'C'  # Celcius
F = 'F'  # Fahrenheit
K = 'K'  # Kelvin


class Temp(object):
    """Temperature value.

    Temp instance can be created in any unit by specifying `units` attribute.

    Can be converted to any unit by using properties: .c. .f, .k

    Currently supported units:
        C - Celcius
        F - Fahrenheit
        K - Kelvin
    """

    def __init__(self, temperature, units='F'):
        """Create new temperature value.

        :param temperature: temperature value in selected units.
        :type temperature: int, float
        :param units: temperature units, allowed values: C, F, K.
        :type units: str
        """

        self.default_units = units

        if units == C:
            self._celcius = float(temperature)
        elif units == F:
            self._celcius = self.f2c(temperature)
        elif units == K:
            self._celcius = self.k2c(temperature)
        else:
            allowed_units = ', '.join(map(lambda u: '"%s"' % u, [C, F, K]))
            msg = 'Unsupported units "{}". Currently supported are: {}.'
            raise ValueError(msg.format(units, allowed_units))

    def _f2c(self, f):
        """Fahrenheit to Celcius."""

        return (f - 32) * 5 / 9.

    def _k2c(self, k):
        """Kelvin to Celcius."""

        return k - 273.15

    def __int__(self):
        return self.c

    @property
    def c(self):
        """Temperature in Celcius."""
        return self._celcius

    @property
    def f(self):
        """Temperature in Fahrenheit."""
        return self._celcius * 9 / 5. + 32

    @property
    def k(self):
        """Temperature in Kelvin."""
        return self._celcius + 273.15

    def __float__(self):
        property_mapping = {C: self.c, F: self.f, K: self.k}
        return property_mapping[self.default_units]
