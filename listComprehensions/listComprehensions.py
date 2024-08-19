#Using a list comprehension, create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers.
# 1回目の回答

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [number for number in numbers if number>0]

print(newlist)

# 模範回答
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)

# 確かに変数名は任意なので短く"x"とする方が見やすい
# integer指定があったが、配列の要素を見てintegerに違いないと決め打ちしたのでキャストしなかったが、要素数が多い時など確信もてるとは限らない時はキャストするべきだろう