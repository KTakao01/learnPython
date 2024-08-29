要点抜粋
1.PythonDocs をざっくりみたかぎり、以下のイメージを持ちました。「すべての例外の基底クラスとして BaseException があり、その派生系として
Exception,ArithmeticError,BufferError,LookupError のベースクラスがある。ベースクラスは具体的に、IndexError、KeyError などのサブクラスがあり、ベースクラスとそのサブクラスの両方を使用できるが、具体的なエラーに対しては通常、サブクラスを用いる。」

```python
def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()
```

2.raise でエラーを任意の場所で発生させられる。
