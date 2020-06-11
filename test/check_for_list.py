# this file will have a function that checks if a value given is a list.

def is_list(val):
    print(type(val))
    return isinstance(val, list)

print(is_list(["Hello", "maker"]))
print(is_list("val"))