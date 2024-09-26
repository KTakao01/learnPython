# The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

# x = object()
# y = object()

x = 1
y = 2

x_list = [x] * 10
y_list = [y] * 10
big_list = [x, y] * 10
big_list2 = x_list + y_list

print(x_list)  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(y_list)  # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(big_list)  # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(big_list2)  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print("x_list contains %d objects" % len(x_list))  # x_list contains 10 objects
print("y_list contains %d objects" % len(y_list))  # y_list contains 10 objects
print("big_list contains %d objects" % len(big_list))  # big_list contains 20 objects

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")  # Almost there...
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")  # Great!
