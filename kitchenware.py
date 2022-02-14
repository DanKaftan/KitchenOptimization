import heapq
import time

import printer


class Kitchenware:

    def __init__(self, capacity, name):
        self.capacity = capacity
        self.dish_list = []
        self.name = name

    # return if there is free space for another dish
    def is_free_place(self):
        return self.capacity > len(self.dish_list)

    def add_dish(self, dish):
        printer.Printer.print_to_terminal(time.ctime() + ": " + "** please put " + dish.dish_type.name
                                          + " in " + self.name + ", remaining place: "
                                          + str(self.capacity - len(self.dish_list)) + " places")
        dish.start_cooking()
        heapq.heappush(self.dish_list, (dish.prepared_date, dish))


    def check_if_there_is_dish_prepared(self):
        if len(self.dish_list) == 0:
            return None
        closest_dish = self.dish_list[0]
        if closest_dish[0] < time.time():
            printer.Printer.print_to_terminal(time.ctime() + ": " "** " +
                                              closest_dish[1].dish_type.name +
                                              " is well cooked! take out of the " + self.name +
                                              ",  remaining place: "
                                              + str(self.capacity - len(self.dish_list) +1) + " places")
            closest_dish[1].set_is_prepared()
            heapq.heappop(self.dish_list)

