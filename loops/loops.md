[Learn Python - Loops](https://www.learnpython.org/en/Loops)

要点
1.python3 では xrange()関数が削除されている。range()関数は、指定された範囲の数値を返す。

```python
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
```

2.for ~ in ... はシーケンス型のオブジェクトに対して使用できるループ。  
(cf)シーケンスとは  
https://www.python.jp/train/tuple/sequence.html

> リスト・タプル・文字列はいずれも コレクション に属するオブジェクトですが、コレクションの一種で、整数値のインデックスを指定して要素を参照できるオブジェクトのことを、シーケンス (Sequence)と呼びます。

```python
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# output
# 2
# 3
# 5
# 7
```

3.while には 2.の制約がなく、あらゆるオブジェクトに適用できて、条件式が true の間はループを続ける。

```python
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
```

4."break"でループを抜ける。"continue"で今のループのブロックをスキップして次のループに進む。

```python
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
```

5.C,C++のように while ループの条件式が false のときに else の処理が実行される。for ループの場合はシーケンスのすべての要素を処理し終えた時に実行される。
ただし,break で抜けたときは while,for ループともに else の処理は実行されない。continue がある場合は else の処理は実行される。
for 文では

````python
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 0,1
    count=0
while(count<5):
    print(count)
    count +=1
    if(count == 2):
        break
else:
    print("count value reached %d" %(count))


# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# Prints out 1,2,3,4,6,7,8,9,9,done
for i in range(1, 10):
    if(i%5==0):
        continue
    print(i)
else:
    print(i)
    print("done")
    ```


Excersiseの所感
最初、奇数判定の条件分岐を前にもってきていて、237の判定を後に持ってきていて失敗しました。
````
