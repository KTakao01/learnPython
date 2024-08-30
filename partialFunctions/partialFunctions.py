# Edit the function provided by calling partial() and replacing the first three variables in func(). Then print with the new partial function using only one input variable so that the output equals 60.
#Following is the exercise, function provided:
# 模範回答
from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7)
print(p(8))

# 私の回答
# from functools import partial
# def func(u, v, w, x):
#     return u*4 + v*3 + w*2 + x
# #Enter your code here to create and print with your partial function
# quad = partial(func,8)
# trpl = partial(quad,8)
# dbl  = partial(trpl,1)
# print(dbl(2))


# 同時に複数の引数を固定できる。左から順に固定されると書いていたのでそこで同時に固定できると気づくべきだった。
