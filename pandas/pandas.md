要点
1.PandasはNumpyで作られており、主要なデータ構造はDataFrameと呼ばれる。DataFrameは、データを表形式で表現する。
2.DataFrameのキーは`XXX.index`で指定できる。
3.PandasはCSVファイルをDataFrameとして読み込める。
4.角カッコを使って、DataFrameの列を指定できる。１次元の角カッコはSeriesとして返される（単一の列）。２次元の角カッコはDataFrameとして返される（複数の列）。
5.角カッコを使うことで行の指定もできる。(ex)XXX[0:2] 0から1までの2行を取得する。
6.データ選択のために`loc`。`iloc`も使用できる。`loc`はラベルベースの指定方法で、行と列のラベルを指定する。
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