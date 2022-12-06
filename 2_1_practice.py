'''nepali = int(input("Enter the marks for nepali :"))
english = int(input("Enter the marks for english :"))
geography = int(input("Enter the marks for geography :"))
maths = int(input("Enter the marks for maths : "))
chemistry = int(input("Enter the marks for chemistry :"))

total = nepali + english + geography + maths + chemistry
percentage = 0
if total > 0:
    percentage = total / 500 * 100

if percentage >= 80:
    print(f"Your percentage is {percentage} and your grade is A+")
elif percentage >= 70:
    print(f"Your percentage is {percentage} and your grade is B+")
elif percentage >= 60:
    print(f"Your percentage is {percentage} and your grade is B")
elif percentage >= 40:
    print(f"Your percentage is {percentage} and your grade is C")
elif percentage >= 35:
    print(f"Your percentage is {percentage} and your grade is D")
else:
    print("Fail")
'''

# ring road area : 27 km every 5 km get the distance (5km - 15rs)
# if student then 10% discount. if kalanki to kalanki full bhada


# area = 27
# from k-s - 5 km
# from s-g - 5km
# from g-k - 5km
# from k-s - 5km


# option 1 kalanki to kalanki 27km * 15rs if student then 10%discount

###########################################################################

# print('''1. Kalanki
# 2. Gaushala
# 3.Koteshwor
# 4.Satdobato
# ''')

# area1 = input("Enter your start position : ")
# area2 = input("Enter your end position : ")
#
# bhada = 0

# if area1 == "1" and area2 == "1" or area1 == "2" and area2 == "2" or area1 == "3" and area2 == "3" or area1 == "4" and area2 == "4":
#     print('''Type 1 for yes and 2 for no''')
#     student = input("Are you student : ")
#     if student == '1':
#         bhada = 15 * 4 / 10
#         print(bhada)
#     else:
#         bhada = 15 * 4
#         print(bhada)
# elif (area1 == "1" and area2 == "2" or area1 == "2" and area2 == "3" or area1 == "3" and area2 == "4") or (
#         area1 == "2" and area2 == "1" or area1 == "3" and area2 == "2" or area1 == "4" and area2 == "3"):
#     print('''Type 1 for yes and 2 for no''')
#     student = input("Are you student : ")
#     if student == '1':
#         bhada = 15 / 10
#         print(bhada)
#     else:
#         bhada = 15
#         print(bhada)
# elif (area1 == "1" and area2 == "3" or area1 == "2" and area2 == "4" or area1 == "3" and area2 == "1") or (
#         area1 == "3" and area2 == "1" or area1 == "4" and area2 == "2" or area1 == "1" and area2 == "3"):
#     print('''Type 1 for yes and 2 for no''')
#     student = input("Are you student : ")
#     if student == '1':
#         bhada = 15 * 2 / 10
#         print(bhada)
#     else:
#         bhada = 15 * 2
#         print(bhada)
# elif (area1 == "1" and area2 == "4" or area1 == "2" and area2 == "1" or area1 == "3" and area2 == "2") or (
#         area1 == "4" and area2 == "1" or area1 == "1" and area2 == "2" or area1 == "2" and area2 == "3"):
#     print('''Type 1 for yes and 2 for no''')
#     student = input("Are you student : ")
#     if student == '1':
#         bhada = 15 * 3 / 10
#         print(bhada)
#     else:
#         bhada = 15 * 3
#         print(bhada)

###########################################################################
# user age : should be greater than 18 and less than 40. if 18 - 25 drink bear if 25 -35 drink wine 35 above any drink

# user_age = int(input("Enter your age : "))

# if user_age >= 18 and user_age <= 40:
#     if user_age >= 18 and user_age <= 25:
#         print('Can drink beer')
#     elif user_age >= 25 and user_age <= 35:
#         print('Can drink wine')
#     else:
#         print('Can drink beer and wine or any other drink')

###########################################################################
# (1 - 9.9 min) bonus tariff
# ntc to ntc - 2.5rs
# ntc to ncell - 5rs
# ncell to ncell - 10rs
# ncell to ncell - 20rs

# print('''Press 1 for All Nepal Ntc Pack''')

# option = input('Enter the option : ')

# if option == '1':
#     print('Congrats all nepal ntc pack is activated')
#     print('''Press 2 to claim your bonus tariff''')
#     option_bonus_claim = input('Enter the key : ')
#     if option_bonus_claim == '2':
#         print('Congrats your bonus tariff is activated')
#         print('''(1 - 9.9 min) bonus tariff
#                 1.ntc to ntc - 2.5rs
#                 2.ntc to ncell - 5rs
#                 3.ncell to ntc - 10rs
#                 4.ncell to ncell - 20rs''')
#         option_bonus = float(input('Enter your last call duration : '))
#         if option_bonus > 0 and option_bonus < 10:
#             option_operator = input('Enter the operator option : ')
#             if option_operator == '1':
#                 print('Congrats 2.5 rs is credited to your account')
#             elif option_operator == '2':
#                 print('Congrats 5 rs is credited to your account')
#             elif option_operator == '3':
#                 print('Congrats 10 rs is credited to your account')
#             elif option_operator == '4':
#                 print('Congrats 20 rs is credited to your account')
#             else:
#                 print('Invalid option')

#     else:
#         print('Sorry your option is not valid')
# else:
#     print('Sorry your option is not valid')


# data = {
#     'name': 'sophia',
#     'age': 12,
#     'phone': 1231231,
#     'address': 'kathmandu',
#     'town': {
#         'name': 'putalisadak',
#         'ward': [
#             [0, 1, 2, 3, 4, 5, 6]
#         ]
#     },
#     'students': {
#         'value': {
#             'name': 'shashank',
#             'cars' : ['lambo','mustang','audi', {'age' : [1,1,2]}]
#         }
#     },
# }


some_dict = {
    'some_no' :  [1,2,3,4]
}

print(some_dict['some_no'])


# 1st method.
# print(data['town']['tole']['name'])

# 2nd method.
# town_obj = data.get('town')
# tole_obj = town_obj.get('tole')
# print(tole_obj.get('name'))


# print(data['town']['ward'][0])
# print(data['students']['value'])
# print(data['students']['value']['cars'][3].get('age')[0])