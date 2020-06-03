class Grabber:
    def __init__(self, func):
        # self.func is the link to the generator
        self.func = func
        self.latest = None

    def next(self):
        print("next")
        self.latest = next(self.func)
        return self.latest
    
    def last(self):
        print("last")
        return self.latest


# count until i
def count(i):
    for x in range(i):
        yield x

g = Grabber(count(5))

print(g.next())
print(g.next())
print(g.last())