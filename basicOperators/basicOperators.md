- [Learn Python - Basic Operators](https://www.learnpython.org/en/Basic_Operators)

  1.算術演算子は他プログラミング言語と同様に使用できる。

```python
number = 1 + 2 * 3 / 4.0
print(number)

# output:2.5
```

以下に例示する。  
・剰余も"%"で求められる。

```python
remainder = 11 % 3
print(remainder)

# output:2
```

・冪乗(power relationship ?)は"\*\*"で求められる。

```python
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# output:
# 49
# 8

```

2.文字列演算子の例  
・文字列結合は"+"で行える。

```python
helloworld = "hello" + " " + "world"
print(helloworld)

# output:
# hello world
```

・文字列の繰り返しは"\*"で行える。

```python
lotsofhellos = "hello" * 10
print(lotsofhellos)
# output:
# hellohellohellohellohellohellohellohellohellohello
```

3.リスト演算子の例。文字列と同様に行える。  
・リストの結合は"+"で行える。

```python
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# output:
# [1, 3, 5, 7, 2, 4, 6, 8]

```

・リストの繰り返しは"\*"で行える。

```python
print([1,2,3] * 3)

# output:
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

練習問題の所感  
・一回間違えた。big_list = [x + y] _ 10 とした。big_list = [x + y] _ 10 として、テストコードと不一致なのに気づいて修正しました。
