# testing the generation features of python.

arr = [5, 4, 3, 2, 1]

def get_tokens(inp):
    for x in inp:
        yield x

gen = get_tokens(arr)

# show the generator object
print(gen)
# get the next token from the generator
print(next(gen))
