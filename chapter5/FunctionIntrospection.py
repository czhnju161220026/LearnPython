from inspect import signature


def my_function(num:int, text:str, num2:'int>0'=80)->str:
    return text + str(num + num2)


if __name__ == '__main__':
    sig = signature(my_function)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ': ', param.name, '=', param.default)


