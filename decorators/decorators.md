[Learn Python - Decorators](https://www.learnpython.org/en/Decorators) 1.デコレータは関数、メソッド、クラスのような呼び出し可能オブジェクトに簡単な変更を加えられる。
(例)以下の二つのコードは同等の意味を持つ。

```python
@decorator
def functions(arg):
    return "value"
```

```python
def function(arg):
    return "value"
function = decorator(function)
```

2.デコレータの定義方法

```python
def repeater(old_function):
    def new_function(*args, **kwds): # See learnpython.org/en/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value
```

ChatGPT の解説で理解した。引用。

```python
コードの流れ
def repeater(old_function):

repeater という関数(デコレータ)を定義しています。
引数として受け取っている old_function は、デコレータを適用した“元の関数”になります。
def new_function(*args, **kwds):

repeater の中で、新しく new_function という関数を定義しています。
*args、**kwds は、可変長引数 (複数の引数) やキーワード引数 (辞書形式の引数) を受け取れるようにするためのものです。
例: my_func(a, b, c=1, d=2) のような呼び出し方に対応するために使われます。
old_function(*args, **kwds) # 1回目

new_function の中で “元の関数” (old_function) を引数つきで呼び出しています。
old_function(*args, **kwds) # 2回目

“元の関数” を再度呼び出しています。
return new_function

repeater は、新しく定義した new_function を「結果として返す」ようになっています。
これによって、@repeater を付けた関数は、実際には new_function が呼び出されることになります。
使い方イメージ
python
コードをコピーする
@repeater
def greet(name):
    print(f"Hello, {name}!")

# greet("Alice") を呼び出すと、実際には greet が 2回呼び出されるので
# 「Hello, Alice!」
# 「Hello, Alice!」
# と2回出力される。
上記のように、@repeater を付ける（デコレータを付与する）と、関数 greet を呼び出したときに、同じ関数処理を2回連続で行います。

```

使い方

```python
>>> @repeater
def multiply(num1, num2):
    print(num1 * num2)

>>> multiply(2, 3)
6
6
```

2-1.実例 2 つ目

```python
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15
```

```python
このコードも「デコレータ (decorator)」を使ったサンプルです。multiply(multiplier) というデコレータ生成関数を用いて、ある関数の返り値を一定倍にして返す、という仕組みを実装しています。

コード全体の流れ
python
コードをコピーする
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator  # it returns the new generator

@multiply(3)  # multiply(3) はデコレータとして働く
def return_num(num):
    return num

print(return_num(5))  # 結果: 15
1. multiply(multiplier)
まず、この関数は デコレータ生成関数 です。
@multiply(3) のように呼び出されると、3 が引数 multiplier に入ります。そして戻り値として、multiply_generator という関数を返します。

multiply(3) が呼ばれると、その戻り値は関数 multiply_generator です。
つまり、最終的にデコレータとして使われるのは multiply_generator という関数になります。
2. multiply_generator(old_function)
multiply_generator は、実際にデコレート対象の関数 (old_function) を受け取り、新しい関数 (new_function) を返す関数です。

ここでは、@multiply(3) を付けた関数を old_function と呼んでいます（例: return_num が old_function に当たります）。
3. new_function(*args, **kwds)
new_function は、実際にデコレータを適用した結果の“置き換わり後”の関数です。
この関数では元の関数 (old_function) を呼び出し、その返り値に multiplier を掛けた結果を返しています。

python
コードをコピーする
def new_function(*args, **kwds):
    return multiplier * old_function(*args, **kwds)
*args, **kwds は、可変長引数および可変長キーワード引数を受け取るためのものです。
ここでは、どんな引数構成の関数でも正しく受け渡しできるように利用しています。
4. return multiply_generator
multiply(multiplier) の末尾で、multiply_generator を返しています。

これによって、@multiply(3) という「(3)を渡した後の結果」をデコレータとして使用できるようになります。
使い方
python
コードをコピーする
@multiply(3)
def return_num(num):
    return num
@multiply(3) は、まず multiply(3) を呼び出します。
すると multiply_generator という関数が返ってきます。
Python は、その返ってきた multiply_generator に対して、return_num 関数を old_function として渡します。
つまり実際には multiply_generator(return_num) という呼び出しが行われています。
その結果 multiply_generator(return_num) は new_function を返し、return_num の定義が new_function で上書きされます。
実行イメージ
python
コードをコピーする
return_num(5)
デコレートされた return_num は new_function になっているので、内部では
python
コードをコピーする
return multiplier * old_function(*args, **kwds)
に従って 3 * return_num(5) (元の関数) を実行し、戻り値として 15 が返ってきます。
まとめ
multiply は デコレータを生成する関数 で、引数として multiplier を受け取る。
返り値として、multiply_generator という デコレータ関数 を返す。
multiply_generator は、元の関数 (old_function) を受け取り、新しい関数(new_function)を返す。
new_function では、元の関数を呼び出して得られた値に multiplier を掛け合わせた値を返す。
デコレータの仕組みの理解に役立つサンプルコードです。
```
