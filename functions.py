def func1(arg):
    arg_temp1 = arg
    arg_temp2 = arg_temp1 / 3
    return (arg_temp1 * arg_temp2)


def func2(arg):
    arg_temp1 = arg[0]
    arg_temp2 = arg_temp1 % 3
    return (arg_temp1 * arg_temp2)

def func3(a):
    a["RemoType"] = 10
    return a["RemoType"]

def func4(lis):
    result = 0
    for i in lis:
        for j in i:
            result = j

# Annotated function
def func5(a: int, b: int , c : str) -> int:
    new_str = c + " " + str(a + b)
    return a + b


call1 = func1(1)
call2 = func2([1, 2.3, 3])


