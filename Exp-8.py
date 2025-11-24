#To write a python program that defines a car class with attributes like make, model, and year and methods like start() to start the car and stop() to stop the car.
class Car:
"""
A class to represent a car.
Attributes:
make (str): The manufacturer of the car.
model (str): The model of the car.
year (int): The manufacturing year of the car.
is_started (bool): True if the car is started, False otherwise.
"""
def __init__(self, make, model, year):
"""
Initializes a new Car object.
Args:
make (str): The manufacturer of the car.
model (str): The model of the car.
year (int): The manufacturing year of the car.
"""
self.make = make
self.model = model
self.year = year
self.is_started = False # Car is initially stopped
def start(self):
"""
Starts the car if it's not already started.
"""
if not self.is_started:
self.is_started = True
print(f"The {self.year} {self.make} {self.model} has started. Vroom! ")
else:
print(f"The {self.make} {self.model} is already running.")
def stop(self):
"""
Stops the car if it's currently running.
"""
if self.is_started:
self.is_started = False
print(f"The {self.year} {self.make} {self.model} has stopped. ")
else:
print(f"The {self.make} {self.model} is already stopped.")
def display_info(self):
"""
Displays the car's information and its current status.
"""
status = "started" if self.is_started else "stopped"
print(f"\n--- Car Information ---")
print(f"Make: {self.make}")
print(f"Model: {self.model}")
print(f"Year: {self.year}")
print(f"Status: The car is currently {status}.")
print(f"-----------------------\n")
# --- Demonstration of the Car class ---
if __name__ == "__main__":
# Create a Car object
my_car = Car("Tesla", "Model 3", 2023)
# Display initial information
my_car.display_info()
# Start the car
my_car.start()
# Try to start it again
my_car.start()
# Display updated information
my_car.display_info()
# Stop the car
my_car.stop()
# Try to stop it again
my_car.stop()
# Create another car
second_car = Car("Honda", "CRV", 2020)
second_car.display_info()
second_car.start()
second_car.display_info()
