要点抜粋  
1.通常、関数の引数の数は事前に宣言される。  
2.＊を引数の前に記載して、可変の引数を設定できる。  
（例）

```python
def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1, 2, 3, 4, 5)
```

3.キーワードで引数を渡すこともできる。ここでは options.get("キーワード")=="キーワードの値" で値を受け取る。

```python
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
```
