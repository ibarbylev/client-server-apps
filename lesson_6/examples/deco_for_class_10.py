"""Function decorator for class
1. Get class instance as function argument
2. Change (rewrite) the class method to the method described in the function decorator
3. Return class instance with modified method
"""


def mod_bar(cls):
    """Decorator as function
    Gets class instance, changes it method and return
    class instance with renew method
    """
    def decorate(func):
        """Return decorated function"""
        def new_func(self):
            """Description of the new (changed) method"""
            print(self.start_str)
            print("Логика декоратора")
            print(func())
            print(self.end_str)

        return new_func

    cls.show = decorate(cls.show)
    return cls


@mod_bar
class Test:
    def __init__(self):
        self.start_str = "Запуск декоратора"
        self.end_str = "Завершение декоратора"

    @classmethod
    def show(cls):
        return "Какая-то функциональность метода класса"


TEST_OBJ = Test()
TEST_OBJ.show()
