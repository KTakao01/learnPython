numpy では subset(配列の部分的な切り出し）機能がありますが、subset の値を変更するときに
その変更の仕方によって、元の配列の値が変更されるかされないか変わってくるというすさまじくややこしい問題があります。

他言語でも普遍的に、同様に値の変更において破壊的かどうかという問題はややこしく、例えば、以下の問題を完璧に説明できる人は少ないのではないでしょうか。以下に値の変更について

1.[イミュータブルオブジェクトにおいては値の変更されているように見えて実際は新しいオブジェクトに再代入しているだけで元の値は直接変更できない](https://qiita.com/rdupejd7c4/items/1109ec84810bb5860121)

2.[ミュータブルオブジェクトにおいては元の値を更新できる](https://qiita.com/rdupejd7c4/items/1109ec84810bb5860121)

3.[シャローコピー](https://developer.mozilla.org/ja/docs/Glossary/Shallow_copy)：新しいオブジェクトを作成して元のオブジェクトと同じ参照を共有してコピーする。 4.[ディープコピー](https://developer.mozilla.org/ja/docs/Glossary/Deep_copy)：新しいオブジェクトを作成して元のオブジェクトと同じ参照を共有せずコピーする。

当初、上記概念が似ているので
イミュータブルオブジェクトの再代入プロセスをメモリアドレスの確保 → ディープコピー → コピー先の値の変更というふうに捉えていましたが、Claude3 によるとどうも違うようで、
メモリアドレスの確保 → 完全に新しいオブジェクトの作成というのが正しいようです。

以下に参考までにコードをおいておきますが、本題から逸れるため飛ばしていただいて構いません。

```python
print("イミュータブルオブジェクト（文字列）の例：")
a = "hello"
print(f"a の初期値: {a}, メモリアドレス: {id(a)}")
b = a
print(f"b = a 後の b の値: {b}, メモリアドレス: {id(b)}")
a += " world"  # 新しいオブジェクトが作成され、aに再代入される
print(f"a += ' world' 後の a の値: {a}, メモリアドレス: {id(a)}")
print(f"操作後の b の値: {b}, メモリアドレス: {id(b)}")

print("\nミュータブルオブジェクト（リスト）の例：")
a = [1, 2, 3]
print(f"a の初期値: {a}, メモリアドレス: {id(a)}")
b = a
print(f"b = a 後の b の値: {b}, メモリアドレス: {id(b)}")
a.append(4)  # aの内容が直接変更される
print(f"a.append(4) 後の a の値: {a}, メモリアドレス: {id(a)}")
print(f"操作後の b の値: {b}, メモリアドレス: {id(b)}")
```

さて余談が過ぎました。
本題のサブセットの話に戻ります。
以下のコードを見てください。
numpy がよくわからない人は[こちら](https://www.learnpython.org/en/Numpy_Arrays)を参考にしてください。

```python
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
print(type(np_height))

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi) # [23.34925219 27.88755755 28.75558507 25.48723993 23.87257618 25.84368152]

# For a boolean response
print(bmi > 23) # [ True  True  True  True  True  True]
print(bmi > 24) # [False  True  True  True False  True]

# Print only those observations above 23

bmi_view = bmi[bmi > 24]
print(bmi_view)  # [27.88755755 28.75558507 25.48723993 25.84368152]
print(bmi) # [23.34925219 27.88755755 28.75558507 25.48723993 23.87257618 25.84368152]

# 元配列の値を変更
bmi_view = bmi[bmi > 24] = 24.0
print(bmi_view) # 24.0
print(bmi) # [23.34925219 24.         24.         24.         23.87257618 24.        ]

# 元配列の値が変更されない
#　インデキシング（ブールインデキシング）
bmi_view2 = bmi[bmi == 24]
print(bmi_view2) # [24. 24. 24. 24.]
bmi_view2[:] = 29.0
print(bmi_view2) # [29. 29. 29. 29.]
print(bmi) #[23.34925219 24.         24.         24.         23.87257618 24.        ]
```

解説は以下の通りです。
python の仕様がわからない方は[こちら](https://docs.python.org/3/reference/datamodel.html#object.__getitem__)を参照してください。

1.bmi_view = bmi[bmi > 24] = 24.0 の場合:

これは **setitem**() 操作に相当します。
bmi > 24 でブール配列が作成され、それを使って bmi の特定の要素を選択します。
選択された要素に直接 24.0 が代入されます。
この操作は元の bmi 配列を直接変更します。
bmi_view には単に 24.0 が代入されます（配列ではありません）。

2.bmi_view2 = bmi[bmi == 24] と bmi_view2[:] = 29.0 の場合:

最初の行は **getitem**() 操作に相当します。
bmi == 24 でブール配列が作成され、それを使って bmi の特定の要素を選択します。
選択された要素の新しいビュー（コピーではない）が bmi_view2 に代入されます。
bmi_view2[:] = 29.0 は bmi_view2 の全要素を 29.0 に変更しますが、これは bmi の元の配列には影響しません。

これの難しいところは「ビューが元の配列と同じアドレスでありながら、ビューの値を変更しても元の配列の値を変更しないようにできる」という先に挙げた既存の言語にない概念にあると思います。この”できる”というのが曲者で、他言語のシャローコピーに似た挙動を示して、「元の配列の値を変更することもできる」というのは強調しておきます。

上記の例をもう少し簡潔にまとめると、以下の通りです。
[]の後に=がくると元の配列の値を変更できるということです。それは**setitem**()を呼んでいるから、ということになります。

```python
import numpy as np

# 元の配列
original = np.array([1, 2, 3, 4, 5])

# ビュー
view = original[original > 2]

print("元の配列:", original)
print("ビュー:", view)

# ビューの変更
view[:] = 10

print("\n変更後:")
print("元の配列:", original)
print("ビュー:", view)

# 直接代入
original[original > 2] = 20

print("\n直接代入後:")
print("元の配列:", original)
print("ビュー:", view)

```

```python
元の配列: [1 2 3 4 5]
ビュー: [3 4 5]

変更後:
元の配列: [1 2 3 4 5]
ビュー: [10 10 10]

直接代入後:
元の配列: [ 1  2 20 20 20]
ビュー: [20 20 20]
```

ちなみにですが、「ビューが元の配列と同じアドレスでありながら、ビューの値を変更しても元の配列の値を変更しないようにできる」というのはメモリ効率がよく、大規模なデータセットにおいては良いパフォーマンスを示すものと思われます。
以上です。
ありがとうございました。
