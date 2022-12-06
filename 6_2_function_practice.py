#1

# def input_func():
#     maths = int(input("Enter the marks for maths : "))
#     chem = int(input("Enter the marks for chemistry : "))
#     phy = int(input("Enter the marks for  phy : "))
#     return maths,chem,phy

# def total():
#     input_marks = input_func()
#     return input_marks[0] + input_marks[1] + input_marks[2]

# def division():
#     total_marks = total()
#     return total_marks/300

# def percentage():
#     return f'Percentage is : {division() * 100}'

# def display():
#     print(percentage())
 
# display()

#2

# def laptop():
#     return " Laptop : Dell laptop, HP laptop, MSI laptop, lenevo laptop, apple laptop"


# def mobile():
#     laptop_items = laptop()
#     return "Mobiles : Apple, Samsung, MI, Oneplus",laptop_items

# def computer():
#     return [mobile()[1],mobile()[0]]
    
# print(" ".join(computer()))


#3

data = [
    {'name' : 'Shashank','age' : 25,'occupation' :'SDE','salary' : 80000},
    {'name' : 'Sujana','age' : 24,'occupation' :'Content-Writer','salary' : 50000},
    {'name' : 'Eshwar','age' : 51,'occupation' :'Manager','salary' : 90000},
]
storage = ''
storage_sal = ''

def search_data(func):
    def search_real_data(name1):
        global storage
        for i in data:
            if i['name'] == name1:
                storage += f'Data was found at {i}'       
        if storage == '':
            return func(name1)
        else:
            return storage
    return search_real_data


def search_salary_check(func):
    def check_range(first_sal,second_sal):
        global storage_sal
        for i in data:
            if i['salary'] >= first_sal and i['salary'] <= second_sal:
                storage_sal += f'{i}' + "\n"
        if storage_sal == "":
            return func(first_sal,second_sal)
        else:
            return storage_sal
    return check_range 
  
@search_data 
@search_salary_check 

def get_name(name):
    return name

def get_sal(firstsal,secondsal):
    return firstsal,secondsal

print(get_sal(14000,80000))
