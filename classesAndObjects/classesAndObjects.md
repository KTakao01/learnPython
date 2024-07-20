[Learn Python - Classes and Objects](https://www.learnpython.org/en/Classes_and_Objects)
要点
1.オブジェクトとは、変数と関数をひとまとめにカプセル化したもの。クラスはオブジェクトを作るためのテンプレート。
2.クラスをオブジェクトにする,そのオブジェクトにアクセスするには以下のようにする。

```python
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass() #クラスをオブジェクトへ

myobjectx.variable #オブジェクトの変数にアクセスする
myobjectx.function() #オブジェクトの関数にアクセスする
```
**3.同じクラスから異なる複数のオブジェクトを作れる。それぞれのオブジェクトには、クラスで定義された変数のコピーが含まれる。**
**4.__init()__はクラスのコンストラクタで、オブジェクトが作られた時（＝クラスのインスタンスが作成される時？）に自動的に呼ばれる。**

```python
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'
```
