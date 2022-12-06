# f = open("sample.txt")
# text = f.read()
# print(text)
# f.close()


# with open("sample.txt") as f:
#     tt = f.read()
#     print(tt)



# f = open('1_1_dictionary.py')
# print(f.read())
# f.close()



f = open('gender_submission.csv')
txt = f.read()
# val = [i.strip("\n") for i in some_list]

val = txt.split('\n')

print(val[10])
f.close()