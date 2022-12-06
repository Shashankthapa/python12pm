# does not allow duplicates.
data = {'name': 'ram', 'age': 20}

# dictionary methods....
'''print(data.get('name'))
keys = data.keys()
values = data.values()
datakey = [i for i in keys]
datavalue = [i for i in values]
print(datakey, datavalue)'''

# read set and dictionaries set up git and github
data1 = {
    'name': "Sujana",
    'address': "Thecho"
}

data = {
    'users': {
        'name': 'shashank', 'age': 20
    }
}

city = {
    'name': 'Eshwar',
    'add': {
        "city": 'kathmandu',
        "est": 1986,
        "gaupalika": {'voda_no': 6 , "population" : 20000}
    }
}
print(city['add']['city'])
print(city['add']['est'])
print(city['add']['gaupalika']['population'])

