#Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures. That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.
# your code goes here
def multiplier_of(multiplicand):
    def multiply_with_number(multiplier):
        ans = multiplier * multiplicand
        print(ans)
        return ans
    return multiply_with_number

multiplywith5 = multiplier_of(5)
multiplywith5(9)

# 外部関数で内部関数を返しておらずエラーにはまっていた。ここは要注意。