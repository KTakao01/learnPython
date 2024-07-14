要点
・pythonはオブジェクト指向言語、静的型付け
・主に次の型をサポート。Numbers:integer,float / Strings /
・Stringはシングル、ダブルクオートの両方を使えるが、アポストロフィーが文字列にあるとき、シングルクオートを使っているとアポストロフィーで終わってしまう（シングルクオートとアポストロフィーは同一文字？なので、基本的にダブルクオートを使った方が楽かも？）

・そのほかのStringsの仕様はpython documentation参照とのこと。気になった点を抜粋
'doesn't'  # use ' to escape the single quote...
>>"doesn't"
シングルクオートのエスケープ

print('C:\some\name')  # here \n means newline!
>>C:\some
ame
print(r'C:\some\name')  # note the r before the quote
>>C:\some\name
改行記号のエスケープ

'"Yes," they said.'
>>'"Yes," they said.'
ダブルクオートは万能ではない

・文字列にも単純な演算子を適用できる

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

・複数の変数に1行で代入可能
a, b = 3, 4

・stringsとnumbersを混同して処理することはできない 

練習問題の所感
・書き方がGoっぽい。