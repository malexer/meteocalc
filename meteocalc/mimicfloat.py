import operator


def math_method(name, right=False):
    def wrapper(self, other):
        value = self.value
        math_func = getattr(operator, name)

        if right:
            value, other = other, value

        result = math_func(value, other)
        return type(self)(result, units=self.units)

    return wrapper


class MimicFloat(type):

    overrride_methods = ('__add__', '__sub__', '__mul__', '__truediv__')
    overrride_rmethods = ('__radd__', '__rsub__', '__rmul__', '__rtruediv__')

    def __new__(cls, name, bases, namespace):
        for method in cls.overrride_methods:
            namespace[method] = math_method(method)

        for rmethod in cls.overrride_rmethods:
            method = rmethod.replace('__r', '__')
            namespace[rmethod] = math_method(method, right=True)

        return super(MimicFloat, cls).__new__(cls, name, bases, namespace)
