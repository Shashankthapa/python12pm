# no_list = [5, 9, 7, 2, 4, 9, 9, 9,4]
# sum = no_list[0] + no_list[-1]
# print(sum)


# count = 0

# for i in range(3, len(no_list)):
#     if no_list[i] == sum:
#         count += 1

# if count == 0:
#     print(f'{sum} is not there in the list.')
# else:
#     print(f"{sum} has occured {count} times")


students = [
    ['rita','gita','sita'],
    ['shashank','sujana','ravi'],
    ['sushma','kavita','chanchal']
]


## for

# for i in students:
#     for j in i:
#         print(j, end = " ")


## while


# i = 0
# while i <= len(students)-1:
#     j = 0
#     while j < len(students[i]):
#         if students[i][j] == "gita" or students[i][j] == "kavita":
#             print(students[i][j])
#         j += 1
#     i += 1

## list comprehension 
# val = [j for i in students for j in i if j == "chanchal" or j == "gita"]
# print(val)


enter_num = int(input("Enter the no : "))
def check_even_odd(enter_num):
    count_even,count_odd = 0,0
    for i in range(0,enter_num):
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_odd,count_even

returned_val = check_even_odd(enter_num)
even_msg = f"There are {returned_val[0]} even nums"
odd_msg = f"there are {returned_val[1]} odd nums"
print(f"{even_msg} and, {odd_msg}")
