要点抜粋
1.python には json(python2.7 以降)という JSON のエンコード、デコードのための組み込みライブラリが備わっている。
JSON データのフォーマットには２種類あり、オブジェクトデータ構造と文字列がある。
オブジェクトデータ型にはデータを削除したり追加、検索するなどのメソッドを使える。
文字列型では主に他のプログラムへのデータ引渡しやデータ構造にロードをする時に用いる。

2.JSON 文字列をデータ構造にデコードするには loads メソッドを用いる。

```python
import json
print(json.loads(json_string))
```

```python
import json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

json.loads('"\\"foo\\bar"')

from io import StringIO
io = StringIO('["streaming API"]')
json.load(io)
```

3.データ構造を JSON 文字列にエンコードするには dumps メソッドを用いる。

```python
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
```

4.pickle という python 独自のシリアライゼーションメソッドもある、

```python
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))
```

＊[シリアライゼーション：データ構造やオブジェクトの状態をメモリやデータベース、他のサービスに保存または送信できる形式に変換するプロセスのことらしい。](https://zenn.dev/fujishiro/scraps/8456c28d7c0fa3)

※[json との比較¶
pickle プロトコルと JSON (JavaScript Object Notation) との基本的な違いは以下のとおりです:

JSON はテキストの直列化フォーマット (大抵の場合 utf-8 にエンコードされますが、その出力は Unicode 文字列です) で、pickle はバイナリの直列化フォーマットです;

JSON は人間が読める形式ですが、pickle はそうではありません;

JSON は相互運用可能で Python 以外でも広く使用されていますが、pickle は Python 固有です;

JSON は、デフォルトでは Python の組み込み型の一部しか表現することができず、カスタムクラスに対しても行えません; pickle は極めて多くの Python 組み込み型を表現できます (その多くは賢い Python 内省機構によって自動的に行われます; 複雑なケースでは 固有のオブジェクト API によって対応できます)。

pickle とは異なり、信頼できない JSON を復元するだけでは、任意のコードを実行できる脆弱性は発生しません。](https://docs.python.org/ja/3/library/pickle.html)

感想
1.pickle はバイトストリームで、バイトコードと同様のバイナリ形式。バイトはコンパイル後、読み取られる形式という例からわかるようにコンピュータ(CPU)にとって効率的な言語。
2.pickle はコンパイルしていないがバイトでやりとりしているので効率的にやりとりできそう

claude3 抜粋

```markdown
pickle と JSON の比較:

速度: 一般的に、pickle は JSON より高速です。特に大きなデータ構造の場合。
用途:

pickle: Python オブジェクトの完全な保存と復元に適しています。
JSON: 異なる言語やシステム間でのデータ交換に適しています。

pickle の使用場面:

機械学習モデルの保存
Python プログラム間でのデータ交換
複雑な Python オブジェクトの一時的な保存

pickle の注意点:

セキュリティ: 信頼できないソースからの pickle データは安全ではありません。
互換性: 異なる Python バージョン間で互換性の問題が発生する可能性があります。
```

3.よくわからないけど信頼できないソースからの pickle 化は危険らしい。CPU が直接読めるバイナリだからコンピュータへの影響範囲が広くなる？
ちょっと違った。
危険性は、pickle の unpickle 処理が Python インタープリタ上で行われ、その過程で任意のコードが実行される可能性があるためです。

claude 回答だとこう。

SQL インジェクションに似てる気がしました。
