# class are blueprint of objects
class Car:
    owner = "Udit Kundu" # class attribute - shared by all the objects
    color = None
    # constructor function
    def __init__(self,name, price, code) -> None:
        self.name = name # instance attribute - different by individual objects
        self.price = price
        self.__code = code # private

    @classmethod 
    # method which is accessable to all the objects, created from this class and even with Class
    def who_is_owner(cls):
        print(f"Owner of the car is {cls.owner}")
    
    # method which is accessable to all the objects from the class but not from the main class
    def color_the_car(self, color):
        self.color = color



car1 = Car("Tesla Model A1", "23,000", 8923)
car2 = Car("Lambogini X43", "45,000", 9998)


print(car1.__code) # you can't access