[Learn Python - Map, Filter, Reduce](https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce)

0.mapはコールバック関数を引数にとり、そのコールバック関数を各要素に対して実行する。
1.mapの戻り値はmap object。listではない
2.コールバック関数に必要な引数の数だけmapに渡す。過不足ある場合は、対応する引数の数だけ反復処理して、エラーは発生せず停止する。
```python
# Python 3

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)
```
3.zipは反復的にタプルを作成する

```python
# Python 3

my_strings = ['a', 'b', 'c', 'd' ]
my_numbers = [1, 2, 3]

results = list(zip(my_strings, my_numbers))

print(results)
```
4.mapは全ての要素を関数を介して渡して、関数を通過した全ての要素の結果を返していましたが、filterはまずtrue,falseを返すための関数を必要として、それから関数を介して反復可能な要素を渡し、falseを返す要素を取り除き、trueを返す要素を残す。
5.filterの引数は一つ。
```python
# Python 3
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
```
6.reduceはコールバック関数をとりそのコールバック関数に引数を累積的に適用する。最初と２番目の要素が関数の引数になり、次の要素はその結果
と３番目の要素になる。initialはreduceの３番目の引数でこれを指定すると、この値から累積的に計算される。

```python
# Python 3
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)
```
7.reduceはfunctoolsモジュールからインポートして使う。
8.reduce は初期値がない場合、リストの先頭要素を初期値として扱い、残りの要素を順に畳み込む。