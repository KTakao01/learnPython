#In this exercise, print an alphabetically sorted list of all the functions in the re module containing the word find.
import re

# Your code goes here
find_members = []
re_members = dir(re)
for re_member in re_members:
    if "find" in re_member:
        find_members.append(re_member)
        
print(sorted(find_members))

# 1回目　ソートし忘れてた
        
        