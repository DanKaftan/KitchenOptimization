import time
import main
import printer


class Order:

    def __init__(self, dishes_list, name):
        self.dishes_list = dishes_list
        self.name = name
        self.MAX_TIME_FOR_START_ORDER = 5
        self.MAX_EXCEPTION_IN_DISHES = 2


    # this method manage the process of preparing the order
    def start_working_on_order(self):
        printer.Printer.print_to_terminal(time.ctime() + ": " + self.name + "'s order entered the kitchen system in:  " + str(time.time()))
        # finds the dish with the longest cooking time send it to funnel
        self.longest_dish = self.find_longest_dish()
        self.send_dish_to_funnel(self.longest_dish)
        self.ready_dishes = 0

    # finds the dish with the longest cooking time in the order
    def find_longest_dish(self):
        longest_dish = self.dishes_list[0]
        for dish in self.dishes_list:
            if dish.dish_type.cooking_time > longest_dish.dish_type.cooking_time:
                longest_dish = dish
        return longest_dish

    def send_dish_to_funnel(self, dish):
        if dish is self.longest_dish:
            self.set_should_start_cooked_date(dish, True, self.MAX_TIME_FOR_START_ORDER)
            main.funnel_dict[dish.dish_type.name].add_dish(dish)
        else:
            self.set_should_start_cooked_date(dish, False, self.MAX_EXCEPTION_IN_DISHES)
            main.funnel_dict["timed_funnel"].add_dish(dish)

    # called when a dish of the order start being cooked
    def notify_dish_start_cooking(self, dish):
        # if the longest dish start cooking send the others to timed_funnel
        if dish is self.longest_dish:
            for other_dish in self.dishes_list:
                if other_dish is not dish:
                    self.send_dish_to_funnel(other_dish)

    def notify_dish_ready(self, dish):
        printer.Printer.print_to_terminal(time.ctime() + ": "+ "** The " + dish.dish_type.name +
                                          " of " + self.name + " is ready, time: " + str(time.ctime()))
        self.ready_dishes += 1
        if self.ready_dishes == len(self.dishes_list):
            printer.Printer.print_to_terminal(time.ctime() + ": " +self.name + "'s order is ready!\n"
                                                          "the difference between the first and last dish was:"
                                              + str(dish.prepared_date - self.find_first_dish_prepared_date()) + " sec")
            if dish.prepared_date - self.find_first_dish_prepared_date() < self.MAX_EXCEPTION_IN_DISHES:
                printer.Printer.print_to_terminal("which is smaller than the exception time which is: " + str(self.MAX_EXCEPTION_IN_DISHES))
            else:
                printer.Printer.print_to_terminal("which is bigger than the exception time which is: " + str(self.MAX_EXCEPTION_IN_DISHES))


    def find_first_dish_prepared_date(self):
        first_dish_prepared_time = self.dishes_list[0].prepared_date
        for dish in self.dishes_list:
            if dish.prepared_date < first_dish_prepared_time:
                first_dish_prepared_time = dish.prepared_date
        return first_dish_prepared_time


    def set_should_start_cooked_date(self, dish, is_longest_dish, exception_time):
        # if the dish is the longest, the start_cooking_time will be now + 10 sec
        if is_longest_dish:
            dish.should_start_cooked_date = time.time() + exception_time
        else:
            # we want the start cooking time to be: longest_order_end_date - this_cooking_time - exception_time
            dish.should_start_cooked_date = self.longest_dish.prepared_date\
                                            - dish.dish_type.cooking_time - exception_time
        printer.Printer.print_to_terminal(time.ctime() + ": " + "The " + dish.dish_type.name + " of " +
                                          self.name + " should start be cooked in: " +
                                          str(time.ctime(dish.should_start_cooked_date)))