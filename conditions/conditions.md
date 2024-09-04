[Learn Python - Conditions](https://www.learnpython.org/en/Conditions)

1.条件の評価は boolean,比較演算子,and/or 演算子,in 演算子,is 演算子,not 演算子などを用いて行う。

boolean 演算：==は変数の代入と記号が似ているので注意する。and/or,比較演算子を使って複雑な演算を行える。

```python
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
# output:
# Your name is either John or Rick.
```

in 演算子：リストなどのオブジェクトに指定されたオブジェクトが含まれているかどうかを調べられる。
補足.if について:コードブロックはインデントで行う。４スペースが通常だが一貫性があれば、他のサイズでも構わない。特別な終了記号や構文（"termination"）が不要。例えば End などが不要

```python
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
```

not 演算子: 条件を反転させられる。

```python
print(not False) # Prints out True
print((not False) == (False)) # Prints out False
```

is 演算子：オブジェクトの同一性を調べられる。

```python
statement = False
another_statement = True
if statement is True:
    # do something
    print('a')
elif another_statement is True: # else if
    # do something else
    print('b')
else:
    # do another thing
    priny('c')

# output
# b
```

補足：ミュータブルオブジェクトでは、シャローコピー

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x
x.append(4)

print("x: {}, id(x): {}".format(x, id(x)))
print("y: {}, id(y): {}".format(y, id(y)))
print("z: {}, id(z): {}".format(z, id(z)))

print("x == y: {}".format(x == y))  # 値の比較
print("x is y: {}".format(x is y))  # 同一性（アドレス）の比較
print("x is z: {}".format(x is z))  # 同一性（アドレス）の比較

# 出力例：
# x: [1, 2, 3, 4], id(x): 140315647943496
# y: [1, 2, 3], id(y): 140315648453768
# z: [1, 2, 3, 4], id(z): 140315647943496
# x == y: False
# x is y: False
# x is z: True
```

補足:イミュータブルオブジェクトではディープコピー

```python
x = 5
y = x
y += 1

print("x: {}, id(x): {}".format(x, id(x)))
print("y: {}, id(y): {}".format(y, id(y)))

print("x == y: {}".format(x == y))
print("x is y: {}".format(x is y))

# 出力例：
# x: 5, id(x): 10914496
# y: 6, id(y): 10914528
# x == y: False
# x is y: False
```

2.Truthy/Falsy
真（True）と評価される場合：

a. ブール値の True が与えられた場合:

```python
x = True
if x is True:
    print("x is Truthy")
else:
    print("x is Falsye")
# 出力: x is Truthy
```

b. 真と評価される算術比較や他の式の結果:

```python
x = 5 > 3
if x is True:
    print("5 is Truthy")
else:
    print("5 is Falsy")
# 出力: 5 is greater than 3
```

c. 空でないオブジェクト:

```python
x = [1, 2, 3]  # 空でないリスト
if x is True:
    print("x is Truthy")
else:
    print("x is Falsy")
# 出力: x is Truthy
```

偽（False）と評価される場合：

a. ブール値の False:

```python
x = False
if x is True:
    print("x is Truthy")
else:
    print("x is Falsy")
# 出力: x is Falsy
```

b. 空と見なされるオブジェクト：
空文字列:

```python
x = ""
if x is True:
    print("x is Truthy")
else:
    print("x is Falsy")
# 出力: x is Falsy
```

空リスト:

```python
x = []
if x is True:
    print("x is Truthy")
else:
    print("x is Falsy")
# 出力: x is Falsy
```

数値の 0:

```python
x = 0
if x is True:
    print("x is Truthy")
else:
    print("x is Falsy")
# 出力: x is Falsy
```

None:

```python
x = None
if x is True:
    print("x is Truthy")
else:
    print("x is Falsy")
# 出力: x is Falsy
```

空の辞書:

```python
x = {}
if x is True:
  print("x is Truthy")
else:
  print("x is Falsy")

# 出力: x is Falsy
```

空のタプル:

```python
x = ()
if x is True:
  print("x is Truthy")
else:
  print("x is Falsy")

# 出力: x is Falsy
```

空の集合:

```python
x = set()
if x is True:
  print("x is Truthy")
else:
  print("x is Falsy")

# 出力: x is Falsy
```

<!--
ポインタないと、イミュータブルかミュータブルでシャローコピーかディープコピーかをわけるのか。よくわかってないけど本題からそれるので頭の片隅に置くだけおいて次に進む。

column.
ポインタないと、イミュータブルかミュータブルでシャローコピーかディープコピーかをわけるのか。よくわかってないけど本題からそれるので頭の片隅に置くだけおいて次に進む。
Claudeさんに聞いてみた。

備忘録

ポインタないから通常、ただたんに変数＝変数とするとその変数は参照渡しされオブジェクトが同じ位置を参照していることになる

Edit
その通りです。素晴らしい観察です。Pythonのこの動作は、他の言語（特にC言語のようなポインタを明示的に扱う言語）と比較すると、少し異なる概念かもしれません。Pythonの変数の振る舞いについて、もう少し詳しく説明しましょう：

Pythonの変数は「名前」:
Pythonでは、変数は実際にはオブジェクトに付けられた「名前」や「ラベル」のようなものです。
代入操作の意味:
a = b のような代入操作は、「aという名前をbが指しているオブジェクトに付ける」という意味になります。
参照の共有:
結果として、aとbは同じオブジェクトを参照することになります。これは、C言語でポインタを共有するのに似ています。
イミュータブル（不変）とミュータブル（可変）オブジェクト:
イミュータブルオブジェクト（整数、文字列、タプルなど）の場合、変更操作は新しいオブジェクトを作成します。
ミュータブルオブジェクト（リスト、辞書など）の場合、変更操作は同じオブジェクトを修正します。
浅いコピーと深いコピー:
単純な代入では浅いコピー（参照のコピー）が行われます。
完全に独立したコピーが必要な場合は、深いコピーを行う必要があります（copy.deepcopy()など）。
例：


# ミュータブルオブジェクト（リスト）の例
a = [1, 2, 3]
b = a  # b は a と同じリストを参照
b.append(4)
print(a)  # [1, 2, 3, 4] - a も変更される

# イミュータブルオブジェクト（整数）の例
x = 5
y = x  # y は x と同じ値を持つが、別のオブジェクト
y += 1
print(x)  # 5 - x は変更されない
print(y)  # 6
この動作はPythonのメモリ管理と密接に関連しており、効率的なメモリ使用を可能にしています。同時に、ミュータブルオブジェクトを扱う際には注意が必要で、意図しない副作用を避けるために、オブジェクトの共有と変更の影響を理解することが重要です。


また出てきたとき裏をとる -->
