def my_function(num:int, text:str, num2:'int>0'=80)->str:
    return text + str(num + num2)

if __name__ == '__main__':
    print(my_function.__annotations__)
    print(my_function(1, 'Hello,', 1))
