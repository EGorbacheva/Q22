from abc import ABC


class Pizza:
    def __init__(self, size: str):
        self.size = size
        self._ingredients = ["сыр", "томатный соус"]
        self.base_price = {"small": 10, "medium": 15, "large": 20}
        self.price = self.base_price.get(size)

    def get_ingredients(self):
        return self._ingredients

    def add_ingredients(self, _ingredients):
        if len(self._ingredients) < 10:
            self._ingredients.append(_ingredients)
        else:
            print("Ингридиентов не может быть больше десяти")

    def calculate_price(self):
        return self.price + len(self._ingredients)


class MeatPizza(Pizza):
    def calculate_price(self):
        return (self.price + len(self._ingredients)) * 1.2


class VeggiePizza(Pizza):
    def calculate_price(self):
        return (self.price + len(self._ingredients)) * 0.9


class Order(ABC):
    def prepare(self):
        pass


class PizzaOrder(Order):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def prepare(self):
        print(f"Готовим пиццу {self._pizza.size}. Ингредиенты: {', '.join(self._pizza._ingredients)}. "
              f"Цена: {self._pizza.calculate_price()}")


class Pizzeria:
    def take_order(pizza_type: str, size: str, extra_ingredients: list):
        if pizza_type.lower() == "meat":
            pizza = MeatPizza(size)
        elif pizza_type.lower() == "veggie":
            pizza = VeggiePizza(size)
        else:
            pizza = Pizza(size)

        for item in extra_ingredients:
            pizza.add_ingredients(item)

        order = PizzaOrder(pizza)
        order.prepare()


Pizzeria.take_order("meat", "large", ["бекон", "пепперони", "грибы"])
Pizzeria.take_order("veggie", "small", ["грибы", "перец"])
