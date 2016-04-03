import sys

from functools import wraps
import operator


PYTHON2 = sys.version_info.major == 2


class FloatCompatible(type):
    """Metaclass to make Temp class compatible with float for basic math.

    This will allow to mix Temp class with floats in basic math expressions
    and return Temp instance in result of the same unit.
    """

    math_methods = [
        '__add__', '__sub__', '__mul__', '__truediv__',
        '__pos__', '__neg__',
    ]
    math_rmethods = ['__radd__', '__rsub__', '__rmul__', '__rtruediv__']

    def __new__(cls, name, bases, namespace):
        if PYTHON2:
            cls.math_methods.append('__div__')
            cls.math_rmethods.append('__rdiv__')

        for method in cls.math_methods:
            namespace[method] = cls.math_method(method)

        for rmethod in cls.math_rmethods:
            method = rmethod.replace('__r', '__')
            namespace[rmethod] = cls.math_method(method, right_operator=True)

        return super(FloatCompatible, cls).__new__(cls, name, bases, namespace)

    @classmethod
    def math_method(cls, name, right_operator=False):
        """Generate method for math operation by name.

        :param name: name of method. i.e. '__add__'
        :param right_operator: is it a "right" operation as '__radd__'
        :type right_operator: bool
        """

        math_func = getattr(operator, name)

        @wraps(math_func)
        def wrapper(*args):
            # [self, other] - binary operators, [self] - unary
            args = list(args)

            self = args[0]
            args[0] = self.value

            if right_operator:
                args = args[::-1]  # args: self, other -> other, self

            result = math_func(*args)
            return type(self)(result, unit=self.unit)

        return wrapper
