[Learn Python - Parsing CSV Files](https://www.learnpython.org/en/Parsing_CSV_Files)

1.csvファイルの読み取り例
```python
以下のコードは、どのように CSV の行を読み取っているかを比較する例です。

Example 1
python
Copy code
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
csvreader から読み取ったすべての行を row に代入してループを回している。
CSV の最初の行（ヘッダー行）も含めてすべての行が print される。
Example 2
python
Copy code
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()  # 1行目を読み込む
    for row in csvreader:
        print(row)
fields = csvreader.next() によって、最初の行（ヘッダー）だけを先に読み込んでしまう。
つまり、イテレータである csvreader を 1行分先に進めている。
その後の for row in csvreader: では、ヘッダー以降の行のみが読み取られる。
結果として、ヘッダー行はループの中で print されず、ヘッダーを除いた行だけが出力される。
なぜこの違いが生まれるのか
Example 1: for row in csvreader: は、ファイルポインタがまだ何も読んでいない状態から始まるため、CSV の最初の行（ヘッダー）も含めて逐次すべてを読み込む。
Example 2: csvreader.next()（Python 3 では next(csvreader) と書くことが多い）の呼び出しによって、すでにヘッダー行を 1回読み取り済みになる。そのため、その後の for row in csvreader: はヘッダー行を飛ばした次の行から処理を始める。
まとめ
Example 1: ヘッダーを含め全行を表示したいとき。
Example 2: ヘッダーをスキップして、データ行のみを処理したいとき。
このように、csvreader は一度イテレートすると戻れないイテレータになっているため、一度 next() を呼ぶとヘッダー行を消費してしまい、その後のループにはヘッダー行が出てこないのがポイントです。
```

