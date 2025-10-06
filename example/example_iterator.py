def printName(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item=next(iterator)
        except StopIteration:
            break
        else:
            print(item)
printName("hello")

def printName(iterable):
    for item in iterable:
        print(item)

printName({"1","2","4","5"})