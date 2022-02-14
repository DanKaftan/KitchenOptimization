import heapq
import time

import funnel

class KitchenwareFunnel(funnel.Funnel):

    def move_closest_dish_to_kitchenware(self):
        while True:
            if len(self.dish_list) != 0 and self.kitchenware.is_free_place():
                self.kitchenware.add_dish(heapq.heappop(self.dish_list)[1])
            time.sleep(0.1)