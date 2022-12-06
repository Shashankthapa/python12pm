# def print_func():
#     print('This is the print function')

# print_func()


# name = 'Shashank'
# age = 21
# occupation = 'Software Engineer'

# def take_inp(name,age,occupation):
#     list1 = list()
#     list1.append(name)
#     list1.append(age)
#     list1.append(occupation)
#     return list1

# print(take_inp(name,age,occupation))


# revise data types,numbers,strings,tuple,set,dictionary
# condition statements
# loops
# functions
# type conversion (int to str)
# modules.
# understand if __name__ == __main__:
# make a tinker app


# optional argument should always be at the end of the function after the regular argument.
# optional argument set's the default value of the argument.
# there can be as many as optional arguments in the function.

# def welcome(course, duration, name, add="Thecho", phone="+977 9828245888"):
#     print(
#         f"Welcome to {course} course {name} and the duration is {duration} months his address is {add} and phone no is {phone}")


# welcome("Python", 2.5, "Shashank" , "ktm", "123")


# def add(num1, num2):
#     print(num1 + num2)
# add(2, 3)


# a = 12,13,14
# print(a)


# SI = P * R * T/100

# def take_value(p,r,t):
#     return p,r,t

# def cal():
#     tk_val = take_value(1000,2,1)
#     return (tk_val[0]*tk_val[1]*tk_val[2])/100,tk_val


# def total_amt_display():
#     disp_cal = cal()
#     return disp_cal[0] + disp_cal[1][0]

# print(total_amt_display())


# cal the percentage.


# def take_inp_sub():
#     maths = int(input("Enter the maths sub : "))
#     chem = int(input("Enter the chem sub : "))
#     phy = int(input("Enter the physics sub : "))
#     return [maths, chem, phy]


# def cal_sum():
#     values = take_inp_sub()
#     total, count = 0,0
#     for i in values:
#         total += i
#         count += 100
#     return total, count


# def percentage():
#     sum = cal_sum()
#     percentage = (sum[0]/sum[1]) * 100
#     return percentage


# print(percentage())


# endless arguments.

# def users(*names, **kwargs):
#     print(names, kwargs)


# users('ram', 'hari', name="shashank", age=12)


# nested functions, lambda functions, recurssion functions,modules,try except finally, file handling,oop


## nested functions 

# def outer_func():
#     print('This is the outer function')
#     def inner_func():
#         print('This is the inner function')
#     inner_func()

# if __name__ == '__main__':
#     outer_func()

    
## lambda functions 

# add = lambda x,y : x + y
# sub = lambda a,b : a - b

# print(add(1,2),sub(1,2))

# set_name = lambda val : val 
# print(set_name('somename'))

# def multiply_2_nos(val1):
#     return lambda val2 : val1 * val2

# mul = multiply_2_nos(2)
# print(mul(3))

## recursion functions

# no = [1,2,3,4,5,1]


# def cal_sum(i):
#     if i == 0:
#         return no[i]
#     else:
#         return no[i] + cal_sum(i-1) 
    

# length = len(no)-1    
# print(cal_sum(length))


#############################

# def user_info():
#     name = input("Enter your name : ")
#     email = input("Enter your email : ")
#     address = input("Enter your address : ")
#     phone = input("Enter your phone : ")
#     return name,email,address,phone

# val = ""
# for i in user_info():
#     val += i + " "
# print(val)

## recursion:


## nested functions 

# def students():
#     def name(naam):
#         return naam
#     return name

# stud1 = students()('Shashank')

# or 

# stud2 = students()
# print(stud1,stud2('Sujana'))

## lamda functions
# lambda functions is used only for one liner

# total = lambda x,y : x + y
# print(f"Total is :{total(10,20)}")


## decorator


def zero_check(func):
    def any_func(a,b):
        if b == 0:
            return "Is equal to zero"
        else:
            return func(a,b)
    return any_func

def check_ab_100(func):
    def any_func(a,b):
        if a > 100 or b > 100:
            return "value of a or b is greater than 100"
        else:
            return func(a,b)
    return any_func

def check_ab_even(func):
    def any_func(a,b):
        if a % 2 == 0 or b % 2 == 0:
            return "value of a or b is even"
        else:
            return func(a,b)
    return any_func

@check_ab_even # check even 
@check_ab_100 # check greater than 100
@zero_check # check if zero or not.

def add(x,y):
    return x+y

print(add(101,11))





















