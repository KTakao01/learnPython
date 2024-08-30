要点抜粋
1.sets は重複のないリストで、例えば、文字列で使われている単語を集めたい場合に使える。

```python
print(set("my name is Eric and Eric is my name".split())) #output: {'and', 'my', 'name', 'is', 'Eric'}
```

2.以下の複数の集合を対象とするメソッドと相性が良い。
intersection（A と B で共通：A かつ B）
synmetric_difference（A もしくは B にのみ含まれる「A かつ<B の否定>」または「B かつ<A の否定>」）
difference(A かつ<B の否定>)
union(A か B に含まれる：A または　 B)

```python
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b)) #output: {'John'}
print(b.intersection(a)) #output: {'John'}
```

```python
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b)) #output: {'Jake', 'Eric', 'Jill'}
print(b.symmetric_difference(a)) #output: {'Jake', 'Eric', 'Jill'}
```

```python
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b)) #output: {'Jake', 'Eric'}
print(b.difference(a)) #output: {'Jill'}
```

```python
a = set(["Jake", "John", "Eric"]) #output: {'Eric', 'Jake', 'Jill', 'John'}
b = set(["John", "Jill"])  #output: {'Eric', 'Jake', 'Jill', 'John'}

print(a.union(b))
```
