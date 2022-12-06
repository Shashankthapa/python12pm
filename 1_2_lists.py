data = ['ram', 'sita', 'geeta', 'hari']
total = len(data)  # length of the element
# print(total)

###############################################

# list methods
# list append

data.append('chotu')
data1 = ['gh', 'matu']
data.append(data1)  # takes the brackets and appends the list
# ignores the brackets and appends the data1 into data
data.extend(data1)

###############################################

# list insert

data.insert(0, 'simon')

# list pop

data.pop()

data.pop(6)  # removes the item from the desired index/

###############################################
# list clear()

# data.clear()

###############################################

# list remove()

data.remove('simon')  # specify the value to be removed
print(data)

# list count

print(f"The no of times the gh is repeated is : {data.count('gh')}")

# data copy

a = 10
b = 12
c = a

# print(id(a), id(c))
copied_data = data.copy()
print(id(copied_data), id(data))


# sorting involves between same type of data
no = [3, 2, 45, 1, 23]
no.sort()
print(no)
# no.sort(reverse=True)
# print(no)
no.reverse()
print(no)
