# inorder to name the files in oop its best to use the capital letters.

class Introduction:
    x = 10
    def get_name(self):
        print("About me : Shashank is my name")

    def get_address(self):
        print("Address : I live in Lalitpur,Thecho")

    def occupation(self):
        print("Occupation : I work as an Software engineer.")

intro = Introduction()
print(intro.x)
intro.get_name()
intro.get_address()
intro.occupation()
