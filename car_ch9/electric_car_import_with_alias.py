# Chapter 9

# Import aliased module.

from electric_car_class_only import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
