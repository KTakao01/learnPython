[Learn Python - List Comprehensions](https://www.learnpython.org/en/List_Comprehensions)
要点
1.list comprehensions はあるリストに基づいて別のリストを作成する手段。
※最初の例を見る限りは普通のリストの作成方法と変わらない気がした。
→ 合っていて、普通のリストの作成方法だった。

```python
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)
```

リスト内包の例

```python
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)
```

※確かにシンプル。慣れが必要そう。
※[式 for 任意の変数名 in イテラブルオブジェクト if 条件式]
