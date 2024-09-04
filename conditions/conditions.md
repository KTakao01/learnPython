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
    print('c')

# output
# b
```

補足：ミュータブルオブジェクト（リスト、辞書など）では、シャローコピー

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

補足:イミュータブルオブジェクト（整数、文字列、タプルなど）ではディープコピー

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
参照の共有:
結果として、aとbはミュータブルオブジェクトでは同じオブジェクトを参照することになります。これは、C言語でポインタを共有するのに似ています。

完全に独立したコピーが必要な場合は、深いコピーを行う必要があります（copy.deepcopy()など）。

この動作はPythonのメモリ管理と密接に関連しており、効率的なメモリ使用を可能にしています。同時に、ミュータブルオブジェクトを扱う際には注意が必要で、意図しない副作用を避けるために、オブジェクトの共有と変更の影響を理解することが重要です。
 -->
