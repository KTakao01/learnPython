#Handle all the exception! Think back to the previous lessons to return the last name of the actor.
import re
# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name(): 
    try:
        actor_name_list = actor["name"].split( )
        last_name = actor_name_list[-1]
        pattern = re.compile(r"[a-zA-Z]+")
        if pattern.fullmatch(last_name) and len(actor_name_list) > 1:
            actor["last_name"] = last_name
            return actor["last_name"]
        else:
            raise ValueError("Last name is not alphabetic.")
    except ValueError as e:
        print("Error: %s" % e)
            
# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())


# 回答
# actor = {"name": "John Cleese", "rank": "awesome"}

# def get_last_name():
#     return actor["name"].split()[1]

# get_last_name()
# print("All exceptions caught! Good job!")
# print("The actor's last name is %s" % get_last_name())