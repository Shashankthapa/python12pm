# tuples are immutable by nature therefore change it to list then append then change to tuple
data = ('rita','shyam','ravi')
data = list(data)
print(data)
data.append('chanchal')
data = tuple(data)
print(data)