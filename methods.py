import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return "Pizza size is : {0}, and ingredients are: {1}".format(self.radius, self.ingredients)
    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


    @classmethod
    def margherita(cls):
        return cls(3,["mozzarella", "tomatoes"])


havana = Pizza(4, ['mozzarella', 'tomatoes'])
print(havana)
print("Size is :{}".format(havana.area()))

print("Classmethod Pizza is: {}".format(Pizza.margherita()))
#print("Classmethod Pizza is: {}".format(Pizza.margherita()))

print("Some circle is: {}".format(Pizza.circle_area(5)))


