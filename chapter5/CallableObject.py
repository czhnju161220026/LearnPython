def f():
    pass


class CallableClass:
    def __call__(self):
        print('Hello world')


if __name__ == '__main__':
    print(type(len))  # builtin function
    print(type(f), type(lambda x: x))  # user's function
    print(type(dict.get))  # method
    print(callable(CallableClass())) # object contains __call__ method
    print(callable(CallableClass))  # class is callable(constructor)
