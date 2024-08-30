[Learn Python - Partial functions](https://www.learnpython.org/en/Partial_functions)
要点
1.python では,部分関数は、functools ライブラリの partial を使う。
左の変数から変数は固定される。

```python
from functools import partial

def multiply(x, y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))
```
