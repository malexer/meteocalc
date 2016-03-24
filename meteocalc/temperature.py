"""Temperature conversion routines."""

from mimicfloat import MimicFloat


C = 'c'  # Celcius
F = 'f'  # Fahrenheit
K = 'k'  # Kelvin


class Temp(metaclass=MimicFloat):
    """Temperature value.

    Temp instance can be created in any unit by specifying `units` attribute.

    Can be converted to any unit by using properties: .c. .f, .k

    Currently supported units:
        C - Celcius
        F - Fahrenheit
        K - Kelvin
    """

    _allowed_units = (C, F, K)
    _conversions = dict(
        # Fahrenheit
        c2f=lambda t: t * 9 / 5. + 32,
        f2c=lambda t: (t - 32) * 5 / 9.,
        # Kelvin
        c2k=lambda t: t + 273.15,
        k2c=lambda t: t - 273.15,
    )

    def __init__(self, temperature, units='C'):
        """Create new temperature value.

        :param temperature: temperature value in selected units.
        :type temperature: int, float
        :param units: temperature units, allowed values: C, F, K.
        :type units: str
        """

        self.units = units.lower()
        self.value = float(temperature)

        if self.units not in self._allowed_units:
            allowed_units = ', '.join(
                map(lambda u: '"%s"' % u.upper(), self._allowed_units)
            )
            msg = 'Unsupported units "{}". Currently supported are: {}.'
            raise ValueError(msg.format(units, allowed_units))

    @classmethod
    def convert(cls, value, from_units, to_units):
        """Convert temperature value between any supported units."""

        from_units = from_units.lower()
        to_units = to_units.lower()

        if from_units == to_units:
            return value

        if from_units != C:
            func_name = '{}2{}'.format(from_units, C)
            f = cls._conversions[func_name]
            value = f(value)

            if to_units == C:
                return value

        func_name = '{}2{}'.format(C, to_units)
        f = cls._conversions[func_name]
        return f(value)

    def _convert_to(self, units):
        return self.convert(self.value, from_units=self.units, to_units=units)

    @property
    def c(self):
        """Temperature in Celcius."""
        return self._convert_to(C)

    @property
    def f(self):
        """Temperature in Fahrenheit."""
        return self._convert_to(F)

    @property
    def k(self):
        """Temperature in Kelvin."""
        return self._convert_to(K)

    def __float__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(float(self))

    def __repr__(self):
        return 'Temp({}, units="{}")'.format(self.value, self.units.upper())
