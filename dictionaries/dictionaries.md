[Learn Python - Dictionaries](https://www.learnpython.org/en/Dictionaries)
要点
1.辞書はキーと値のペアを格納するデータ型。(=ハッシュマップ?)。
**2.辞書は反復処理するとき、順序を保持しない。キーと値をセットでループするときは、items()を用いる。**
``` python
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
```

(cf)値をループするには.values()を用いる。キーをループするには.keys()を用いる。
# https://www.kikagaku.co.jp/kikagaku-blog/python-for-dictionary/

3.辞書から項目を削除するにはdelかpopを用いる。
``` python
del phonebook["John"]
phonebook.pop("John")
```
