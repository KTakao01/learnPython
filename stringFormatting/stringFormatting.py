# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

# 1回目
data = ("John", "Doe", 53.44)
format_string = "Hello"

print("Hello %s %s. Your current balance is $%s." % data)