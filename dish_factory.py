import dish
import dish_type

# the DishFactory responsible for create new dishes by their given name
class DishFactory:
    dishes_types_dict = {"Burger": dish_type.DishType("Burger", 30, None),
                         "Fries": dish_type.DishType("Fries", 10, None),
                         "Coke": dish_type.DishType("Coke", 1, None)}

    @staticmethod
    def createDish(dish_name, order):
        if dish_name in DishFactory.dishes_types_dict.keys():
            return dish.Dish(DishFactory.dishes_types_dict[dish_name], order)
        else: return None


