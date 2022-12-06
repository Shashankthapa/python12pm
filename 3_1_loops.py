# while, #for loops

###############################################################################

# for a in range(0,5):
#     print(f"'h' + {a}")
#     if a == 3:
#         continue
#     print(f"'a' + {a}")

###############################################################################

# find the occurance of the even no's and odd no's in a list

# x = 0
# count = 0
# count1 = 0
# while x <= 10:
#     if x % 2 == 0:
#         count += 1
#     else:
#         count1 += 1
#     x += 1

# print(f"There are {count} even no's from 0 to 10 and There are {count1} odd no's from 0 to 10")

###############################################################################

# insert the values in the list and then print the values from the list.

# name_inp = 0
# val = []
# while name_inp < 5:
#     value = input('Enter the input : ')
#     val.append(value)
#     name_inp += 1

# for names in val:
#     print(names, end = " ")

###############################################################################

# find the occurance of the values specified in the list.

# count = 0
# name_inp = 0
# val = []
# while name_inp < 5:
#     value = input('Enter the input : ')
#     val.append(value.lower())
#     name_inp += 1

# print(val)
# mylist = list(dict.fromkeys(val))

# count = 0
# for i in mylist:
#     for j in val:
#         if i == j:
#             count += 1
#     print(f"{i} has occured {count} times")
#     count = 0



