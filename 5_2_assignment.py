# def dell(),hp(),lenevo()
# mp_rep (name,times)
# data[] create a function that accepts the data and inserts in the list if data value is repeated then cannot accept.

# 1
# global total_laptop_cost

# toshiba_price = 38000
# dell_price = 50000
# hp_price = 45000
# lenevo_price = 40000

# def take_inp():
#     print("1. Dell(50k) 2.Toshiba(38k) 3.Hp (45k) 4.Lenevo(40k)")
#     which_laptop = int(
#         input("Enter the name of the laptop which you want to buy : "))
#     if which_laptop == 1:
#         dell()
#     elif which_laptop == 2:
#         toshiba()
#     elif which_laptop == 3:
#         hp()
#     elif which_laptop == 4:
#         lenevo()
#     else:
#         print("The option is not right")


# def dell():
#     print('Thanks for choosing Dell please enter the quantities for the laptops 50k for a unit.')
#     print_grand_total(dell_price)


# def toshiba():
#     print('Thanks for choosing Toshiba please enter the quantities for the laptops')
#     print_grand_total(toshiba_price)


# def hp():
#     print('Thanks for choosing Hp please enter the quantities for the laptops')
#     print_grand_total(hp_price)


# def lenevo():
#     print('Thanks for choosing Lenevo please enter the quantities for the laptops : ')
#     print_grand_total(lenevo_price)


# ##################################

# def quantity():
#     quanti = int(input("Enter the quantity : "))
#     return quanti

# def price_cal_laptop(price, quantity):
#     return price * quantity


# def delivery_cost(quant):
#     print('1. Delivery cost : 1000 2. Pickup : Free')
#     option_delivery = int(input("Enter the option : "))
#     if option_delivery == 1:
#         del_cost = 1000 * quant
#     else:
#         del_cost = 0
#     return del_cost


# def packing_costing():
#     print('1.Plastic(Rs 100) 2.Bag(Rs 500) 3.Gift_Box(Rs 1500) 4. None')
#     option_packing = int(input("Enter the option : "))
#     if option_packing == 1:
#         packing_cost = 100
#     elif option_packing == 2:
#         packing_cost = 500
#     elif option_packing == 3:
#         packing_cost = 1500
#     elif option_packing == 4:
#         packing_cost = 0
#     return packing_cost


# def tax_costing():
#     print('1.Inside the valley : 10% Tax 2.Outside the valley : 13%')
#     tax_option = int(input("Enter the value : "))
#     if tax_option == 1:
#         tax = total_laptop_cost * 0.10
#     else:
#         tax = total_laptop_cost * 0.13
#     return tax


# def print_grand_total(laptop_price):
#     global total_laptop_cost
#     quant = quantity()
#     total_laptop_cost = price_cal_laptop(laptop_price, quant)
#     del_cost = delivery_cost(quant)
#     packing_cost = packing_costing()
#     tax_cost = tax_costing()

#     grand_total = total_laptop_cost + del_cost + packing_cost + tax_cost
#     print(f"Total cost is {grand_total}")


# take_inp()

###############################################################################

# 2

# def print_name(name,times):
#     for i in range(0,times):
#         print(name, end = " ")

# print_name('Shashank',10)

# def find_occurance(names,times):
#     for name in names:

# append_list()

#############################################################
# 3 data[] create a function that accepts the data and inserts in the list if data value is repeated then cannot accept.

# data_list = []
# def func():
#     flag = True
#     while flag:
#         value = input("Enter the input :")
#         data_list.append(value)
#         for i in range(len(data_list)):
#             for j in range(len(data_list)):
#                 if i != j:
#                     if data_list[i] == data_list[j]:
#                         flag = False
#                         print("There exist a duplicate end the loop")
#                         break
#             if flag == False:
#                 break

# func()
        

