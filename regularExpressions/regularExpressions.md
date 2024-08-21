要点抜粋

1.正規表現はテキストのパターン一致を見るためのツール。python では re モジュールを使用する。
正規表現の応用範囲は広いがかなり複雑なので代替手段を考え、最後の手段として使用する。

2.（例）` r"^(From|To|Cc).*?python-list@python.org" ``To: !asp]<,. python-list@python.org `の場合
\*python docs から解説を抜粋した。
"^"は行の始まり
"|"は OR
"."は任意の文字（改行記号を除く）
"\*"は直前の文字の 0 回以上の文字の繰り返し
"?"は直前の文字の 1 回の繰り返しか、0 回繰り返し（つまり非表示）
"+"は直前の文字の 1 回以上の繰り返し
"\w"は単語文字に一致。`[a-zA-Z0-9_]`とイコールらしい。`.+`は特殊記号などその他の文字すべて

（例）

```python
# Example:
import re
pattern = re.compile(r"\[(on|off)\]") # Slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-("))
# Doesn't return anything.
# End Example
```

"\"はエスケープ

※re.complile()とは？
Claude3 によると・・・

```python
import re

# パターンをコンパイル
pattern = re.compile(r'\d+')

# コンパイルされたパターンを使用
result1 = pattern.search('abc123def')
result2 = pattern.findall('123abc456')

# これは以下と同等ですが、パターンを複数回使用する場合はより効率的です
# result1 = re.search(r'\d+', 'abc123def')
# result2 = re.findall(r'\d+', '123abc456')
```
