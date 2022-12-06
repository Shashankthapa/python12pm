def register():
    print('Please register you dont have an account')
    obj_write = open('filehandling/database.txt','w')
    name = input("Enter the username : ")
    password = input("Enter the password : ")
    obj_write.write(name + " " + password)
    print('Registration successful')

def login():
    obj_read = open('filehandling/database.txt','r')
    name = input("Enter the username : ")
    password = input("Enter the password : ")
    if name + " " + password in obj_read.read():
        print('Login successful')
    else:
        register()

login()