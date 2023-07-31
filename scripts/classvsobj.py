

# instance == variable 
# class == type
# when you create an instance of a class, the constructor of the class is called first __init__()
# when you call a function you are passing 'arguments'/'parameters' they are short-lived
# meaning they go away when the function ends. 
# if you need to save them, you have save them as data members (sel.*)

class Car:
    # constructor
    def __init__(self, name):
        self.myname = name

    def say_hello(self):
        print(f"Hello, {self.myname}!")

    def start(self):
        print('started')

    # stateful
    def stop(self,message):
        print(f'stopped: {message}')

    # stateless
    def class_function():
        print('I am free of any instance')

class Animal:
    def __init__(self, color, size):
        self.mycolor = color
        self.mysize = size
    
    def grow(self, factor):
        self.mysize = self.mysize * factor
        return self.mysize


# Create a class that represents a grocery store with the following methods and attributes:
# Class:
# Store(name: str, city: str)
# Defines attributes name: str and city: str. Also defines at attribute stock: dict which is itself a dictionary and stores information about each stock item also as a dictionary. For example, stock = {"Bread": {"count": 500, "price": 3.99}}.
# Methods:
# add_to_stock(name: str, count: int, price: float) -> None
# Adds stock item to stock: dict. If stock item already exists, it should add count to the existing count and update price to price. Otherwise, a new stock item {name: {"count": count, "price": price}} should be added to stock: dict.
class Store:

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.stock = {} # defines at attribute stock
    
    def add_to_stock(self, name, count, price):
        if name in self.stock:
            self.stock[name]["count"] += count
            self.stock[name]["price"] = price

        else:
            self.stock[name] = {"count": count, "price": price}

    def remove_from_stock(self, name, count):
        if name not in self.stock:
            raise KeyError("Item not in stock!")

        elif self.stock[name]["count"] < count:
            raise ValueError("Not enough items in stock!")
        
        else:
            self.stock[name]["count"] += count

    def total_store_value(self, name, count, price):
        total_value = 0
        if name in self.stock:
            for name in self.stock:
                value = self.stock[name]["count"] * self.stock[name]["price"]
                total_value += value
            return total_value
        else:
            KeyError("Item not in stock!")

# Test
item = Store("saveon", "Vancouver")
print(item.name)
print(item.city)
print(item.stock)

item.add_to_stock("steak", 200, 68.99)
item.add_to_stock("sourdough", 500, 8.99)
print(item.stock)

item.add_to_stock("sourdough", 200, 10.99)
print(item.stock)

#item.remove_from_stock("cereal", 100)
item.remove_from_stock("steak", 222)

item.total_store_value