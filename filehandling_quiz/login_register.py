def register_heading():
    with open('file.txt', 'w') as op_write:
        op_write.write('ID ')
        op_write.write('name ')
        op_write.write('Phone ')
        op_write.write('Address \n')

def register_content():
    with open('file.txt', 'a') as op_write:
        while True:
            stop = input('Enter stop to exit : ')
            if stop != "stop":
                id = input('Enter the id : ') + "  "
                op_write.write(id)
                name = input('Enter the name : ') + "  "
                op_write.write(name)
                phone = input('Enter the phone no : ') + "  "
                op_write.write(phone)
                address = input('Enter the address : ') + "  " + "\n"
                op_write.write(address)
            else:
                break


def search():
    name = input('Enter the name to be searched : ') + "  "
    return name 

def read():
    op_read_again = open('file.txt','r')
    return op_read_again.read()

def display():
        op_read = open('file.txt','r')
        str_name = search()    
        if str_name in op_read.read():
            print("User exists with the same name.")
            register_content()
        else:
            print(f"{str_name.strip(' ')} does not exist")
            print(read())
        op_read.close()

register_heading()
register_content()
display()
