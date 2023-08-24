"""
* Ingredient Factory:
* 		Design a PizzaIngredientFactory to create pizza ingredients (Cheese, Sauce, Toppings) based on different types of pizzas.
"""

class PizzaIngredientFactory:
    def createIngredient(self, pizzaType):
        if pizzaType == "Cheese":
            return Cheese()
        elif pizzaType == "Sauce":
            return Sauce()
        elif pizzaType == "Toppings":
            return Toppings()
        else:
            return None

class Cheese:
    def getIngredient(self):
        print("Cheese")

class Sauce:
    def getIngredient(self):
        print("Sauce")

class Toppings:
    def getIngredient(self):
        print("Toppings")

def main():
    factory = PizzaIngredientFactory()

    cheese = factory.createIngredient("Cheese")
    sauce = factory.createIngredient("Sauce")
    toppings = factory.createIngredient("Toppings")

    ingredients = [cheese, sauce, toppings]
    for ingredient in ingredients:
        ingredient.getIngredient()

if __name__ == "__main__":
    main()
