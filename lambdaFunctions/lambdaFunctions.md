[Learn Python - Lambda functions](https://www.learnpython.org/en/Lambda_functions)
要点  
1.普通、関数は def キーワードで定義していつでも必要な時に呼び出せる。  
ラムダ関数は、同じ場所で１度だけ使うために定義されるインライン関数。

2.ラムダ関数は別名、匿名関数と呼ばれ、lambda キーワードを使って定義する。
~~※第一級関数みたいなもんか。~~
→ 定義が曖昧で正式な用語ではないし、その使用も難しい。 1.関数を引数のように使用できる 2.式の中で定義ができる 3.型が割り当てられていて他の型と自由に組み合わせられる。

```python
your_function_name = lambda inputs : output
```

通常の関数

```python
def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)
```

ラムダ関数

```python

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)
```

※claude によるとラムダ関数＝第一級関数らしい。以下の特徴を持つ。
無名関数（Anonymous function）：名前を持たない関数のこと。
関数リテラル：その場で定義され、通常は一度だけ使用される短い関数。
クロージャ：自身が定義されたスコープの変数にアクセスできる関数。
高階関数の引数や戻り値として使用される関数。
