def gen_names(name, num):
    i = 1
    while i < num:
        yield name
        i += 1
ranger = gen_names('Ivan Petrov', 50)
names = [x for x in ranger]
print(names)