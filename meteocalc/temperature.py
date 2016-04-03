"""Temperature conversion routines."""

from .classutils import FloatCompatible


C = 'c'  # Celsius
F = 'f'  # Fahrenheit
K = 'k'  # Kelvin


# support metaclass both in Python 2 and 3
AbstractTemp = FloatCompatible('AbstractTemp', (object, ), {})


class Temp(AbstractTemp):
    """Temperature value.

    Temp instance can be created in any unit by specifying `unit` attribute.
    Can be converted to any unit by using properties: .c. .f, .k

    Currently supported units:
        C - Celsius
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

    def __init__(self, temperature, unit='C'):
        """Create new temperature value.

        :param temperature: temperature value in selected units.
        :type temperature: int, float
        :param unit: temperature unit, allowed values: C, F, K.
        :type unit: str
        """

        self.unit = unit.lower()
        self.value = float(temperature)

        if self.unit not in self._allowed_units:
            allowed_units = ', '.join(
                map(lambda u: '"%s"' % u.upper(), self._allowed_units)
            )
            msg = 'Unsupported unit "{}". Currently supported units: {}.'
            raise ValueError(msg.format(unit, allowed_units))

    @classmethod
    def convert(cls, value, from_units, to_units):
        """Convert temperature value between any supported units.

        Conversion is performed using Celsius as a base unit.
        i.e. Fahrenheit -> Kelvin will be converted in two steps: F -> C -> K

        :param value: temperature value
        :type value: int, float
        :param from_units: source units ('C', 'F', 'K')
        :param to_units: target units ('C', 'F', 'K')
        :rtype: float
        """

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

    def _convert_to(self, unit):
        return self.convert(self.value, from_units=self.unit, to_units=unit)

    @property
    def c(self):
        """Temperature in Celsius."""
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

    def __round__(self, n=0):
        return round(self.value, n)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return 'Temp({}, unit="{}")'.format(self.value, self.unit.upper())
