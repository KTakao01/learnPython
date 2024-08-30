[Variables and Types](https://www.learnpython.org/en/Variables_and_Types)
要点  
・python はオブジェクト指向言語、動的型付け言語。変数を用いる前に宣言する必要がなく、型を宣言する必要もない。python のすべての変数はオブジェクト。
・主に次の型をサポート。Numbers:integer,float / Strings /  
・String はシングル、ダブルクオートの両方を使える。ただし、アポストロフィーが文字列にあるとき、シングルクオートを使っているとアポストロフィーまでが対象範囲とされてしまうし、ダブルクオートが文中にあるときは文中のダブルクオートとされてしまう。

・そのほかの Strings の仕様は [python documentation 参照](https://docs.python.org/3/tutorial/introduction.html#strings)とのこと。気になった点を抜粋

```python
>>>'doesn\'t'  # use \' to escape the single quote...
"doesn't"

>>>"doesn't"  # ...or use double quotes instead
"doesn't"

>>>'"Yes," they said.'
'"Yes," they said.'

>>>"\"Yes,\" they said."
'"Yes," they said.'

>>>'"Isn\'t," they said.'
'"Isn\'t," they said.'
```

・文字列にも単純な演算子を適用できる

```python
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
```

・複数の変数に 1 行で代入可能

```python
a, b = 3, 4
```

・strings と numbers を混同して処理することはできない

練習問題の所感  
・書き方が Go っぽい。
