[Learn Python - Modules and Packages](https://www.learnpython.org/en/Modules_and_Packages)
要点
1.モジュールは特定の機能を持つソフトウェアの一部。モジュールはそれぞれ別のファイル。
2.モジュール名.モジュールの関数でそのモジュールの関数を呼び出す。
3.import文の指示で、まず実行した呼び出し元のスクリプトファイルとと同一のディレクトリの.pyファイルを探し、次に組み込みモジュールから探す。
以下のように任意のディレクトリも指定できる。
```python
PYTHONPATH=/foo python game.py
```
fooディレクトリにあるgame.pyファイルを探している。

```python
sys.path.append("/foo")
```
importコマンドを実行するまえに上記を実行することでfooディレクトリが、インポートの検索パスに追加される。

**4.モジュールをインポートすると.pyはpycにコンパイルされる。.pycファイルはpythonバイトコード。これはモジュールがロードされるたびにファイルをパースする必要がないように行う。.pycファイルがある場合、.pyファイルの代わりにこちらがロードされる。**
5.インポート方法
```python 
import <module_name>
<module_name>.<function_name>()
```

```python
from <module_name> import <function_name>
```

```python
from <module_name> import *
```


名前空間には同名のオブジェクトを持つことができない。
以下、Claudeより引用。
```python
def draw_game():
    print("Local draw_game function")

from draw import draw_game  # この行で上の定義が上書きされる

draw_game()  # draw モジュールの draw_game が呼ばれる
```

(cf))
プログラミング言語でサフィックスとは文字の最後尾に書く意味のある文字列のこと( 拡張子が代表的) 今回は .py のことを .py suffixと言っている
# https://discord.com/channels/1084280443945353267/1215189047161659464/1221839099468578906


（cf）
if __name__ == '__main__'::

これは Python の慣用句で、スクリプトが直接実行されたときにのみ特定のコードブロックを実行するために使用されます。
モジュールが他のスクリプトにインポートされた場合、この条件は False となり、ブロック内のコードは実行されません。

6.importを条件分岐でわけることで、以下のような応用ができる。

環境変数をどのように設定するか知りたかったのでclaude3の応答を全文掲載。まあ次案件でDjangoを使うため多分わかるようになると思う。

```python
この例で if visual_mode: という行は、条件付きインポート（conditional import）を示しています。visual_mode は、プログラムの動作モードを決定するブール型（True または False）の変数であると想定されています。
この構造の目的と動作を詳しく説明します：

条件付きインポート:

プログラムの実行時の条件に基づいて、異なるモジュールをインポートすることができます。


visual_mode 変数:

この変数は、プログラムがビジュアルモード（グラフィカルな表示）で動作するか、テキストモードで動作するかを決定します。
通常、この変数はスクリプトの開始時に設定されるか、コマンドライン引数やコンフィグファイルから読み込まれます。


モジュールの選択:

visual_mode が True の場合：
import draw_visual as draw
グラフィカルな描画を行うモジュールがインポートされます。
visual_mode が False の場合：
import draw_textual as draw
テキストベースの出力を行うモジュールがインポートされます。


共通のインターフェース:

どちらのモジュールも draw という名前でインポートされるため、draw.draw_game(result) という呼び出しは、選択されたモードに関わらず同じ形で使用できます。


柔軟性と拡張性:

この方法により、プログラムの core logic を変更することなく、異なる表示モードを簡単に切り替えることができます。



実際の使用例：
pythonCopy# 例えば、コマンドライン引数で visual_mode を設定する
import sys

visual_mode = "--visual" in sys.argv

# 条件付きインポート
if visual_mode:
    import draw_visual as draw
else:
    import draw_textual as draw

def main():
    # ... ゲームのロジック ...
    result = play_game()
    draw.draw_game(result)  # モードに応じて適切な描画が行われる

if __name__ == "__main__":
    main()
この設計により、同じゲームロジックを使用しながら、異なる環境や要件に応じて適切な表示方法を選択することができます。例えば、グラフィカルインターフェースが利用可能な環境では視覚的に豊かな表示を、コンソール環境ではテキストベースの表示を使用するといった柔軟性が得られます。 CopyRetryClaude does not have the ability to run the code it generates yet.Tvisual_mode = "--visual" in sys.argvとは？ Editvisual_mode = "--visual" in sys.argv という行は、コマンドライン引数を確認して、プログラムの動作モードを設定するPythonの表現です。詳しく説明しましょう：

sys.argv:

sys モジュールの argv リストは、Pythonスクリプトに渡されたコマンドライン引数を含みます。
sys.argv[0] はスクリプト名自体で、sys.argv[1]以降が実際の引数になります。


"--visual" in sys.argv:

これは、"--visual" という文字列が sys.argv リストの中にあるかどうかをチェックします。
結果はブール値（True または False）になります。


visual_mode =:

この結果を visual_mode 変数に代入します。



動作の例：

ビジュアルモードで実行する場合:
Copypython script.py --visual
この場合、"--visual" が sys.argv に含まれるので、visual_mode は True になります。
通常モードで実行する場合:
Copypython script.py
この場合、"--visual" は sys.argv に含まれないので、visual_mode は False になります。

この方法の利点：

ユーザーがコマンドライン引数を使って、プログラムの動作モードを簡単に切り替えられます。
プログラム内で条件分岐を使用して、異なる動作を実装できます。

実際の使用例：
pythonCopy
import sys

visual_mode = "--visual" in sys.argv

if visual_mode:
    print("Running in visual mode")
    # ビジュアルモード用のコード
else:
    print("Running in text mode")
    # テキストモード用のコード

# プログラムの残りの部分...
この技術は、同じプログラムに複数の動作モードを実装する際に非常に有用です。ユーザーは簡単にモードを切り替えられ、開発者は1つのスクリプトで複数の機能を提供できます。
```

7.モジュールが実行中の呼び出し元モジュールでロードされた時、コード実行によりモジュールは初期化される。別のモジュールで同じモジュールを再度インポートしても、再度ロードされることはない。
そのためモジュール内のローカル変数はSingletonとして動作する。

```claude
モジュールの再インポート:

同じモジュールが他の部分で再度インポートされても、そのモジュールは再度ロードされません。
代わりに、既にメモリにロードされているモジュールが使用されます。
```

```python
# draw.py

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main_screen as a singleton
main_screen = Screen()
```

```claude3
main_screen オブジェクトは、このモジュールを使用するすべてのコードで共有されます。
アプリケーション全体で一貫したスクリーンオブジェクトを使用できます。
```

8.組み込みモジュールは(該当のモジュールをインポート後？)dirやhelp関数で詳細を表示できる。
9.パッケージには__init__.pyというファイルがある。

mypackage/
    __init__.py
    bar.py
    foo.py
    internal_module.py

```python
__init__.py:

__all__ = ["bar"]
```


```claude
__init__.py ファイルの役割:

このファイルはディレクトリをPythonパッケージとして認識させるために使用されます。
パッケージが初期化されるときに実行されるコードを含むことができます。

__all__ 変数:

この変数はリストで、パッケージから import * を使用した際にインポートされるモジュール名やオブジェクト名を指定します。


__all__ = ["bar"] の意味:

このパッケージから from package import * を使用してインポートした場合、bar モジュール（または名前）のみが公開されることを示します。

API の制御:

これにより、パッケージの作者は公開したいインターフェース（API）を明示的に定義できます。
パッケージ内の他のモジュールや名前は、明示的にインポートしない限り非公開（内部的）に保たれます。
```

