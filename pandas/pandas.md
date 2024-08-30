[Learn Python - Pandas Basics](https://www.learnpython.org/en/Pandas_Basics)
要点
1.Pandas は Numpy で作られており、主要なデータ構造は DataFrame と呼ばれる。DataFrame は、データを表形式で表現する。
2.DataFrame のキーは`XXX.index`で指定できる。
3.Pandas は CSV ファイルを DataFrame として読み込める。 4.角カッコを使って、DataFrame の列を指定できる。１次元の角カッコは Series として返される（単一の列）。２次元の角カッコは DataFrame として返される（複数の列）。 5.角カッコを使うことで行の指定もできる。(ex)XXX[0:2] 0 から 1 までの 2 行を取得する。 6.データ選択のために`loc`。`iloc`も使用できる。`loc`はラベルベースの指定方法で、行と列のラベルを指定する。
`iloc`はインデックスベースの指定方法で、インデックス番号を指定する。

(ex)

```python
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
```
