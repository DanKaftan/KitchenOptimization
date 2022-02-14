import heapq
import time

import funnel
import main


class TimedFunnel(funnel.Funnel):

    def move_closest_dish_to_kitchenware_funnel(self):
        while True:
            if len(self.dish_list) != 0 and (self.dish_list[0])[0] < time.time():
                main.funnel_dict[(self.dish_list[0])[1].dish_type.name].add_dish((self.dish_list[0])[1])
                heapq.heappop(self.dish_list)
            time.sleep(3)