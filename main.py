import threading
import time

import funnel
import kitchen
import kitchenware_funnel
import main
import order_maker
import printer
import timed_funnel


restaurant_kitchen = kitchen.Kitchen()

funnel_dict = {"Burger" : kitchenware_funnel.KitchenwareFunnel(main.restaurant_kitchen.grill),
               "Fries" : kitchenware_funnel.KitchenwareFunnel(main.restaurant_kitchen.frier),
               "Coke" :  kitchenware_funnel.KitchenwareFunnel(main.restaurant_kitchen.drinking_machine),
               "timed_funnel": timed_funnel.TimedFunnel(None)}


def take_orders_loop():
    while True:
        order_maker.OrderMaker.commit_order()
        time.sleep(3)

if __name__ == '__main__':

    print("Hi cashier! Welcome to the restaurant!")
    printer.Printer.print_to_terminal("Starting program!")

    take_orders_loop = threading.Thread(target=main.take_orders_loop)
    check_if_dishes_prepared_loop = threading.Thread(target=main.restaurant_kitchen.check_if_dish_prepared)
    move_closest_burger_to_kitchenware_loop = threading.Thread(target=main.funnel_dict["Burger"].move_closest_dish_to_kitchenware)
    move_closest_fries_to_kitchenware_loop = threading.Thread(target=main.funnel_dict["Fries"].move_closest_dish_to_kitchenware)
    move_closest_coke_to_kitchenware_loop = threading.Thread(target=main.funnel_dict["Coke"].move_closest_dish_to_kitchenware)
    move_waiting_dishes_to_funnels_loop = threading.Thread(target=main.funnel_dict["timed_funnel"].move_closest_dish_to_kitchenware_funnel)

    take_orders_loop.start()
    check_if_dishes_prepared_loop.start()
    move_closest_burger_to_kitchenware_loop.start()
    move_closest_fries_to_kitchenware_loop.start()
    move_closest_coke_to_kitchenware_loop.start()
    move_waiting_dishes_to_funnels_loop.start()