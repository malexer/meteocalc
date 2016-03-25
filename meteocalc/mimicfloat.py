from functools import wraps
import operator


def math_method(name, right_operator=False):
    math_func = getattr(operator, name)

    @wraps(math_func)
    def wrapper(*args):
        args = list(args)  # [self, other] - binary operators, [self] - unary
        self = args[0]
        args[0] = self.value

        if right_operator:
            args = args[::-1]  # args: self, other -> other, self

        result = math_func(*args)
        return type(self)(result, units=self.units)

    return wrapper


class MimicFloat(type):

    math_methods = (
        '__add__', '__sub__', '__mul__', '__truediv__',
        '__pos__', '__neg__',
    )
    math_rmethods = ('__radd__', '__rsub__', '__rmul__', '__rtruediv__')

    def __new__(cls, name, bases, namespace):
        for method in cls.math_methods:
            namespace[method] = math_method(method)

        for rmethod in cls.math_rmethods:
            method = rmethod.replace('__r', '__')
            namespace[rmethod] = math_method(method, right_operator=True)

        return super(MimicFloat, cls).__new__(cls, name, bases, namespace)
