[Learn Python - Conditions](https://www.learnpython.org/en/Conditions)

1.条件の評価、比較は比較演算子で行う。  
2.変数の代入と記号が似ているので注意する。  
**3.in演算子でリストなどのオブジェクトに指定されたオブジェクトが含まれているかどうかを調べられる。**  
4.コードブロックはインデントで行う。４スペースが通常だが一貫性があれば、他のサイズでも構わない。特別な終了記号や構文（"termination"）が不要。ex)Endなど  

5.ちょっと理解に自信ない。  
True,空でないオブジェクトはTrueとして評価される  
空文字、空のリスト、0、FalseはFalseとして評価される。  

```
A statement is evaulated as true if one of the following is correct: 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 2. An object which is not considered "empty" is passed.

Here are some examples for objects which are considered as empty: 1. An empty string: "" 2. An empty list: [] 3. The number zero: 0 4. The false boolean variable: False
```

6.is演算子でオブジェクトの同一性を調べることができる。  
```python 
x = [1,2,3]
y = [1,2,3]
z = x
x.append(4)
print(x == y) # Prints out True
print(x is y) # Prints out False
print(x is z) # Prints out True
print(x) # [1, 2, 3, 4]
```

ポインタないと、イミュータブルかミュータブルでシャローコピーかディープコピーかをわけるのか。よくわかってないけど本題からそれるので頭の片隅に置くだけおいて次に進む。  

column.  
ポインタないと、イミュータブルかミュータブルでシャローコピーかディープコピーかをわけるのか。よくわかってないけど本題からそれるので頭の片隅に置くだけおいて次に進む。  
Claudeさんに聞いてみた。  

備忘録

ポインタないから通常、ただたんに変数＝変数とするとその変数は参照渡しされオブジェクトが同じ位置を参照していることになる

Edit
その通りです。素晴らしい観察です。Pythonのこの動作は、他の言語（特にC言語のようなポインタを明示的に扱う言語）と比較すると、少し異なる概念かもしれません。Pythonの変数の振る舞いについて、もう少し詳しく説明しましょう：

Pythonの変数は「名前」:
Pythonでは、変数は実際にはオブジェクトに付けられた「名前」や「ラベル」のようなものです。
代入操作の意味:
a = b のような代入操作は、「aという名前をbが指しているオブジェクトに付ける」という意味になります。
参照の共有:
結果として、aとbは同じオブジェクトを参照することになります。これは、C言語でポインタを共有するのに似ています。
イミュータブル（不変）とミュータブル（可変）オブジェクト:
イミュータブルオブジェクト（整数、文字列、タプルなど）の場合、変更操作は新しいオブジェクトを作成します。
ミュータブルオブジェクト（リスト、辞書など）の場合、変更操作は同じオブジェクトを修正します。
浅いコピーと深いコピー:
単純な代入では浅いコピー（参照のコピー）が行われます。
完全に独立したコピーが必要な場合は、深いコピーを行う必要があります（copy.deepcopy()など）。
例：


# ミュータブルオブジェクト（リスト）の例
a = [1, 2, 3]
b = a  # b は a と同じリストを参照
b.append(4)
print(a)  # [1, 2, 3, 4] - a も変更される

# イミュータブルオブジェクト（整数）の例
x = 5
y = x  # y は x と同じ値を持つが、別のオブジェクト
y += 1
print(x)  # 5 - x は変更されない
print(y)  # 6
この動作はPythonのメモリ管理と密接に関連しており、効率的なメモリ使用を可能にしています。同時に、ミュータブルオブジェクトを扱う際には注意が必要で、意図しない副作用を避けるために、オブジェクトの共有と変更の影響を理解することが重要です。


また出てきたとき裏をとる


7.not演算子で条件を反転させられる。  
