import time

import kitchenware


class Kitchen:
    def __init__(self):
        # kitchenwares
        self.grill = kitchenware.Kitchenware(4, "Grill")
        self.frier = kitchenware.Kitchenware(4, "Frier")
        self.drinking_machine = kitchenware.Kitchenware(2, "Drinking machine")

    def check_if_dish_prepared(self):
        while True:
            self.grill.check_if_there_is_dish_prepared()
            self.frier.check_if_there_is_dish_prepared()
            self.drinking_machine.check_if_there_is_dish_prepared()
            time.sleep(0.1)

