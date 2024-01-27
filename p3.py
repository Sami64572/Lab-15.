class DecoratorMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")

        for attr_name, attr_value in dct.items():
            if callable(attr_value):  
                print(f"Decorating method: {attr_name}")
                dct[attr_name] = cls.decorate_method(attr_value)

        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def decorate_method(method):
        
        def wrapper(*args, **kwargs):
            print(f"Additional logic before calling method: {method.__name__}")
            result = method(*args, **kwargs)
            print(f"Additional logic after calling method: {method.__name__}")
            return result

        return wrapper

    def __call__(cls, *args, **kwargs):
        print(f"Creating instance of class: {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=DecoratorMeta):
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

obj = MyClass(42)
obj.display()