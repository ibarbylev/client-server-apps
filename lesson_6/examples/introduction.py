def func_decorator(func):
    pass


class ClassDecorator:
    pass

    def __call__(self, func):
        pass


"""1. Function decorator for function"""


@func_decorator
def function():
    pass


"""2. Class decorator for function"""


@ClassDecorator()
def function():
    pass


"""3. Function decorator for class"""


@func_decorator
class SomeClass:
    pass


"""4. Class decorator for class"""


@ClassDecorator()
class SomeClass:
    pass
