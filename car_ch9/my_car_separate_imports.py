
# Chapter 9

# Importing Classes
# Importing from Multiple Modules

from car_class_only import Car
from electric_car_class_only import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
