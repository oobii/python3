t = 1, 2, 3

print(type(t))

t = tuple(range(25))
print(type(t))
print(t)

x = list(range(25))
print(type(x))
x[10] = 42
print(x)

print("x len={}".format(len(x)))

t.index(5)

# how many '5'
t.count(5)

x.append(100)
print("x len={}".format(len(x)))

x.extend(range(22))
print("x len={} , {} ".format(len(x), x))

x.insert(0, 25)
print("x len={} , {} ".format(len(x), x))

# removes element with value of '12'
x.remove(12)
print("x len={} , {} ".format(len(x), x))

del x[12]
print("x len={} , {} ".format(len(x), x))

x.pop()
print("x len={} , {} ".format(len(x), x))

x.pop(0)
print("x len={} , {} ".format(len(x), x))

# Dictionary

# creating a dictionary
d = {'one': 1, 'two': 2}

dd = dict(one=1, two=2)

dict5 = dict(three=3, four=4, five=5)

# creating from another dictionary
ddd = dict(one=1, two=2, **dict5)
print(ddd)

'four' in x

for k in d:
    print(k)

for k, v in d.items():
    print(k, v)

# dont use subscript
#  x['three']

print("using get method, the key is {}".format(d.get('three', 'not there')))

print("using get method, {}".format(ddd.get('three')))

del d['four']

d.pop('five')