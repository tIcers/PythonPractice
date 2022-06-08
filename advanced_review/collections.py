from collections import Counter

from collections import defaltdict
lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

# count numbers

print(Counter(lst))

# counter with string

print(Counter('aabsbsbsbhshhbbsbs'))

# counter with words in sentence

s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
print(Counter(words))

# find most common

c = Counter(words)
print(c.most_common(3))

# defalt dictionary

d = defaltdict(object)

d['one']
for i in d:
    print(i)


def defaltdict():
    return None


class Counter:
    pass


d = defaultdict(lambda: 0)
print(d['one'])

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])

sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")

print(sam[0])