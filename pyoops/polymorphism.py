class Vehicle:
    def speed(self):
        # This is a generic method, which may be overridden by child classes
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def speed(self):
        return "The car speed is 120 km/h."

class Bike(Vehicle):
    def speed(self):
        return "The bike speed is 80 km/h."

class Train(Vehicle):
    def speed(self):
        return "The train speed is 150 km/h."

def show_speed(vehicle):
    # This function demonstrates polymorphism by calling the speed() method
    print(vehicle.speed())

# Example usage:
car = Car()
bike = Bike()
train = Train()

show_speed(car)    # Demonstrates polymorphism with the Car class
show_speed(bike)   # Demonstrates polymorphism with the Bike class
show_speed(train)  # Demonstrates polymorphism with the Train class
