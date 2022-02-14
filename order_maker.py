import os
import time

import dish_factory
import order
import printer


class OrderMaker:

    @staticmethod
    def commit_order():
        # get client's order
        print (time.ctime() + ": " +"first, please write customer's name, to close the cash box write 'stop':")
        name = raw_input()
        if name == "stop":
            print("Good night cashier! see you tomorrow!")
            printer.Printer.clean_file()
            os._exit(1)
        print(time.ctime() + ": " + "please ask "+ name + " what he want to order from this menu:!\nTHE MENU:\n1.Burger\n2.Fries\n3.Coke\n"
               "please write the order with ',' between each dish")
        output_list = raw_input().split(", ")

        # create new order from client's order and start cooking
        dishes_list = [] #list of the orders's dishes
        new_order = order.Order(dishes_list, name)
        for str in output_list:
            new_dish = dish_factory.DishFactory.createDish(str, new_order)
            if new_dish is not None:
                dishes_list.append(new_dish)
            else:
                print (time.ctime() + ": "+ "sorry we dont sell " + str + " please make new order: ")
                return None
        new_order.start_working_on_order()
        print(time.ctime() + ": "+ name + " order's sent to the chef and in progress right now\n")

