# inorder to name the files in oop its best to use the capital letters.

# class Introduction:
#     x = 10 # property or attribute

#     # methods/behaviours
#     def get_name(self):
#         print("About me : Shashank is my name")

#     def get_address(self):
#         print("Address : I live in Lalitpur,Thecho")

#     def occupation(self):
#         print("Occupation : I work as an Software engineer.")

#     def phone_no(self):
#         print("My phone no is : 123xxxxx")

# intro = Introduction()
# print(intro.x)
# intro.get_name()
# intro.get_address()
# intro.occupation()
# intro.phone_no()



# class Calculator:

#     def add(self,num1,num2):
#         return num1 + num2
#     def sub(self,num1,num2):
#         return num1 - num2
#     def div(self,num1,num2):
#         return num1 / num2
#     def mul(self,num1,num2):
#         return num1 * num2


# cal = Calculator()
# print(f"Addition is : {cal.add(1,2)}")
# print(f"Subtraction is : {cal.sub(1,2)}")
# print(f"Division is : {cal.mul(1,2)}")
# print(f"Multiplication is : {cal.div(1,2)}")


class Calculator:
    num1,num2 = 10,3
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def div(self):
        return self.num1 / self.num2
    def mul(self):
        return self.num1 *self.num2


cal = Calculator()
print(f"Addition is : {cal.add()}")
print(f"Subtraction is : {cal.sub()}")
print(f"Division is : {cal.mul()}")
print(f"Multiplication is : {cal.div()}")