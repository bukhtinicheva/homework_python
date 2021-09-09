import random
import string

letters=[]
name='Ivan Petrov Alexandrovich'

print(name)

while name:
    xl= name[:1]
    letters.append(xl)
    name = name[1:]

random.shuffle(letters)

name =''.join(letters)
name=name.lower()
print(name.title())