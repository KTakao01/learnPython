[Learn Python - Code Introspection](https://www.learnpython.org/en/Code_Introspection)
要点
1.Code Introspection により、クラス、関数、キーワードを調べて、その正体、挙動、影響？（＝何を知っているか）を知れる。
以下にそのリストを記載。

```python
help()
dir()
hasattr()
id()
type()
repr()
callable()
issubclass()
isinstance()
__doc__
__name__
```

上記のうち一部抜粋して説明
dir()

https://qiita.com/SAKD/items/bee463de53ecbdf574c6

```python
class Sample():
    def __init__(self, number):
        self.value = number
    def tenfold(self):
        return self.value * 10
a = Sample(10)
print(dir(a))
```

```python
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__weakref__', 'tenfold', 'value']
#dir()はオブジェクトの有効な属性のリストを返した
```

hasattr()
オブジェクトが指定された名前の属性を持っているかどうかを返す。

```python
>>> class Fruit:
...     tasty = True
...
>>> fruit = Fruit()
>>> if hasattr(fruit, 'tasty'):
...     print('The fruit is tasty')
... else:
...     print('The fruit is not tasty')
...
The fruit is tasty
```

id()
オブジェクトの識別子(メモリアドレス）を返す。

```python
a = 2
b = 1
id(a)
140339209865072
id(b)
140339209865096
```
