import time

class Dish:

    def __init__(self, dish_type, order_observer):
        self.dish_type = dish_type # the type of the dish, include its properties
        self.should_start_cooked_date = 0 # the date when dish should start being cooked
        self.prepared_date = 0 # the date when dish will be prepared
        self.is_prepared = False
        self.order_observer = order_observer


    # called when the dish gets out of the funnel and starts being cooked
    def start_cooking(self):
        # calc the end_cooking_time of this dish
        self.prepared_date = time.time() + self.dish_type.cooking_time
        # notify the order that this dish start being cooked
        self.order_observer.notify_dish_start_cooking(self)


    def set_is_prepared(self):
        self.order_observer.notify_dish_ready(self)
        self.is_prepared = True
