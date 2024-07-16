[Learn Python - Basic String Operations](https://www.learnpython.org/en/Basic_String_Operations)

要点
1.文字列はテキストの一部（よくわからない）

2.シングルクオーテーションを出力したいならダブルクオートで囲む
→variablesAndTypes.md参照.

3.文字列のインデックスは0から数える。

4.文字列の個数はcount()で調べられる。
**5.文字列の範囲指定は[start:end]で行う。startは含む、endは含まない。start~end-1番目の文字を出力する。**
→忘れてた。

5.インデックスが負の数は末尾から数える。

**6. [start:stop:step]で間隔を指定して特定範囲から文字列を抽出する**

```python
astring = "Hello world!"
print(astring[3:7]) //lo w
print(astring[3:7:1]) //lo w
```

**7.文字列の反転は[::-1]で行う。**

8.大文字、小文字に変換するにはupper()、lower()を使用する。

9.前方、後方で部分一致するかどうかはstarswith()、endswith()を使用する


```python
astring = "Hello world!"
print(astring.startswith("Hello")) //True
print(astring.endswith("asdfasdfasdf")) //False
```

**10.文字列を分割してリストに格納するにはsplit()を使用する。**  


