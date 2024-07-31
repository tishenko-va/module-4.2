def test_function(x):
    d = x + 1
    def inner_function(x):
        nonlocal d
        if d > 2:
            print("Я в области видимости функции test_function")
    inner_function(x)
    return d
print(test_function(4))
#print(inner_function(4))  #Выдает ошибку NameError: name 'inner_function'
                         # is not defined. Did you mean: 'test_function'?