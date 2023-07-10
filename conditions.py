bool_expr = 6.6 and (5+0.5) and True and "RemoType"
if (bool_expr):
    z = True
else:
    z = 5.9
test_1 = 1
bool_test = True
if (isinstance(bool_test, bool)):
    new_var = test_1
else:
    new_var = "str"

test_2 = new_var
test_3 = z

if 8 > 9:
    del test_3
else:
    test_3 = 5.5


# IfExp
if_exp = 1 if True else 2
if_exp2 = 1 if False else 2.5
if_exp3 = 'RemoType' if True else 2.5