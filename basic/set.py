# s = {5,2,3,'haha', 'hrhe'}
s = {1,3}

s.add(2)
print(type(s))
print(s)
s.update([4,5])
print(s)

## delete set
s.discard(3)
print(s)

s.remove(5)
print(s)

s.pop()
print(s)
s.clear()
print(s)

## Set Operations

a = {1,2,3,4}
b = {3,4,5,6}

print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)

print(a ^ b)

print(a.issubset(b))
