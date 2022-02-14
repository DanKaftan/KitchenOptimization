import heapq
import time

import printer


class Funnel:

    def __init__(self, kitchenware):
        self.dish_list = []
        self.kitchenware = kitchenware

    def add_dish(self, dish):
        heapq.heappush(self.dish_list, (dish.should_start_cooked_date, dish))
        printer.Printer.print_to_terminal(time.ctime() + ": "+ dish.dish_type.name + " added successfully to funnel!")
