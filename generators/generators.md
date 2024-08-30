[Learn Python - Generators](https://www.learnpython.org/en/Generators)
要点
「python プロフェッショナル大全」
(cf)反復処理可能なデータをイテレーターと呼ぶ。例えばリストや辞書など。イテレーターの要素を in で次々取り出し、要素がなくなったらループを終了できるのが for ループ。
ジェネレーターはイテレーターと同じ反復処理だが、要素を取り出すときにその都度要素を生成する。（あらかじめ要素が用意されていない）

1.ジェネレーターは反復可能なアイテムを一回に一つずつ返す。for 文でアイテムをセットして反復処理が始まるとジェネレーターが実行される。
ジェネレーターが yield 文に到達すると、ジェネレーターはその実行を for ループに戻して、セットから新しい値を返す。（どういうこと？）
ジェネレータは好きなだけ値を生成して、それぞれを順番に生産できる。

演習の所感 1.合ってたけど、ジェネレータは for ループでないと使えないと思っていたこと、値を２つ返しているのが一般的でないと、やや回答と異なる結果に。
以下は回答。

```python
# fill in this function
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
```

・while 1: は無限ループを作成
・yield はジェネレーターの状態を保存する。次に関数が呼ばれたとき、yield の直後から実行が再開されます。
