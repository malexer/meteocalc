from functools import wraps
import operator


def math_method(name, right=False):
    math_func = getattr(operator, name)

    @wraps(math_func)
    def wrapper(self, other):
        value = self.value

        if right:
            value, other = other, value

        result = math_func(value, other)
        return type(self)(result, units=self.units)

    return wrapper


class MimicFloat(type):

    math_methods = ('__add__', '__sub__', '__mul__', '__truediv__')
    math_rmethods = ('__radd__', '__rsub__', '__rmul__', '__rtruediv__')

    def __new__(cls, name, bases, namespace):
        for method in cls.math_methods:
            namespace[method] = math_method(method)

        for rmethod in cls.math_rmethods:
            method = rmethod.replace('__r', '__')
            namespace[rmethod] = math_method(method, right=True)

        return super(MimicFloat, cls).__new__(cls, name, bases, namespace)
