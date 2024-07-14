[Learn Python - Loops](https://www.learnpython.org/en/Loops)

要点
1.python3ではxrange()関数が削除されている。
2.for ~ in ... はシーケンス型のオブジェクトに対して使用できる。
cf)シーケンスとは
https://www.python.jp/train/tuple/sequence.html
>リスト・タプル・文字列はいずれも コレクション に属するオブジェクトですが、コレクションの一種で、整数値のインデックスを指定して要素を参照できるオブジェクトのことを、シーケンス (Sequence)と呼びます。

3.whileには2.の制約がない。条件式がtrueの間はループを続ける。

4."break"でループを抜ける。"continue"で次のループに進む。

**5.C,C++のようにループの条件式がfalseのときにelseの処理が実行される。ただし,breakで抜けたときにelseの処理は実行されない。**

```python
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
    ```

これは知りませんでした。

Excersiseの所感
最初、奇数判定の条件分岐を前にもってきていて、237の判定を後に持ってきていて失敗しました。