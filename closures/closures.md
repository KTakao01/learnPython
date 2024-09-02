要点 1.クロージャはメモリに存在していなくてもスコープ内の値を保持している関数オブジェクトのこと。後述するが、外部関数を実行しても内部関数は自動的に実行されない。内部関数が実行されていない状態でも、外部関数のローカル変数の値を記憶しているということ。
→ 補足：メモリに存在していないというのは、内側の関数では引数を渡していないのでメモリにないが外側の引数を用いてアクセスできるということ？
→Claude 回答：通常の関数では関数の実行が終わるとその関数のローカル変数（＝引数、関数内で定義される変数）はメモリから解放される。
クロージャでは内部関数が外部関数のローカル変数を参照している場合、それらの変数は内部関数と一緒に閉じ込められる。そして、内部関数が存在する限りメモリに保持される。
→ 補足：内部関数が存在する条件とは何か？
→Claude 回答：関数定義時はまだ存在していない。外部関数の実行時、内部関数が返されるか、変数に代入された時に、内部関数は存在し始める。
内部関数への参照が維持されている限り、内部関数は存在し続ける。

```python
def outer():
    x = 10
    def inner():
        print(x)
    return inner

func = outer()  # innerがfuncに代入され、ここで「存在」し始める
func()  # 10が出力される
del func  # funcへの参照を削除。この時点でinnerは「存在」**しなくなる可能性がある**
```

inner 関数は outer が呼び出され、func に代入されたときに「存在」し始める。
del func で func への参照を削除すると、inner への参照もなくなり、「存在」しなくなる可能性がある。

(1)関数を呼び出す場合

```python
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    data_transmitter()
print(transmit_to_space("Test message"))

#output
Test message
None
```

(2)関数オブジェクトを返す場合

```python
def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()
transmit_to_space("Burn the Sun!")()
```

transmit_to_space("Test message") が実行される →transmit_to_space 関数のスコープが作成される →
message パラメータに "Test message" が割り当てられます。→data_transmitter 関数が定義されます。この時点で data_transmitter は「存在」し始める。

data_transmitter 実行時：data_transmitter() が呼び出されます。この時、内部関数は既に存在しており、実行される。
ransmit_to_space 終了時：data_transmitter の実行が終わると、transmit_to_space 関数も終了する。この時点で data_transmitter への参照はなくなり、通常はメモリから削除される。ガベージコレクションの対象となる。

→ まとめるるとどうも「外部関数が実行されて（変数、引数を外部関数から受け取るなどして）内部関数の定義が定まった時、もしくは変数に代入された時、つまり関数オブジェクトがメモリ上に作成されて、アクセスできるようになった時に内部関数は存在し始める。単に外部関数内に定義があるだけでは内部関数は存在していない。
外部関数が実行されて初めて内部関数が作成される。」

→ ダメおしの回答：

```python
def outer():
    print("外部関数の実行開始")
    def inner():
        print("内部関数")
    print("内部関数の定義完了")
    return inner

print("outer関数の定義完了")
func = outer()  # この時点でinnerが「存在」し始める
func()  # 内部関数を実行
```

outer 関数が定義されるが、この時点では inner はまだ「存在」していない。
func = outer()が実行されると：

"外部関数の実行開始" が出力される。
inner 関数が定義され、この時点で「存在」し始める。
"内部関数の定義完了" が出力される。
inner 関数が返され、func に代入される。

func()で内部関数が実行される。

2."nonlocal"キーワードを使うと、nonlocal 文が使われた関数の外側のスコープにある変数を、関数の内側のスコープで 変更できる。
[qiita 参考記事](https://qiita.com/domodomodomo/items/6df1419767e8acb99dd7)

```python
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)

```

nonlocal number がある場合の出力は 3,3 だが、ない場合の出力は 3,9 になる。
→ 補足：number という変数が関数の内側についていることで、関数の外側にある number を内部関数の number で変更できる。

→Claude 回答によるダメおし：
nonlocal number がある場合：

内部関数 printer()内の number は外部関数 print_msg()の number を参照する。
number = 3 で外部関数の number の値を 3 に変更する。
出力は 3, 3 になる。

nonlocal number がない場合：

number = 3 は内部関数 printer()のローカル変数 number を新たに作成する。
外部関数の number は変更されない。
出力は 3, 9 になる。

→ 補足：Python では変数の宣言を行わず変数に値を代入した時点で変数が作成されるが、同名の変数を複数回代入可能で、let（再代入）,const（二つ別々に定義）のような２通りに似た挙動が可能

3.クロージャはグローバル変数の使用を避け、データ隠蔽を行える。クラス内にメソッドが少ない場合、代わりにクロージャを使える。また、python のデコレータはクロージャを多用する
