class vehicle:
    def __init__(self, type, year, make, model, doors, roof):
        self.type = type
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

class automobile(vehicle):
    def __init__(self, car, year, make, model, doors, roof):
        super().__init__(car, year, make, model, doors, roof)

user_type = input("Please enter your vehicle type: ")
user_year = input("Please enter the year of your vehicle: ")
user_make = input("Please enter the make of your vehicle: ")
user_model = input("Please enter the model of your vehicle: ")
user_doors = input("Please enter the number of doors your vehicle has: ")
user_roof = input("Please enter the type of roof your vehicle has: ")

user_vehicle = vehicle(user_type, user_year, user_make, user_model, user_doors, user_roof)

print("Vehicle type: " + user_vehicle.type)
print("Year: " + user_vehicle.year)
print("Make: " + user_vehicle.make)
print("Model: " + user_vehicle.model)
print("Number of doors: " + user_vehicle.doors)
print("Type of roof: " + user_vehicle.roof)

