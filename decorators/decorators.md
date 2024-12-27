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
