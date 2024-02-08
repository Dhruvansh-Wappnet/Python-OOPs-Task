"""Vehicle Rental System"""

class Vehicle:
    def __init__(self,vehicle_type,model,year):
        self.vehicle_type = vehicle_type
        self.model = model
        self.year = year
        self.days = 0
        # self.rental_price_per_day = rental_price_per_day
  
    def rent(self,days):
        if self.available == True:
            self.available = False
            self.days = days
            return f"You have successfully rented {self.vehicle_type} for {days} days."
        else:
            return "Sorry, the vehicle is not available at this time."
    
    def return_vehicle(self):
        if self.available == False:
            self.available = True
            return "The car has been returned."
        else:
            return "This car hasn't been out for rent yet."
        
    def calculate_rental_fee(self):
        pass
        
class Car(Vehicle):
    num_car = 0
    
    def __init__(self,vehicle_type,model,year):
        Car.num_car += 1
        if Car.num_car <= 2:
            super().__init__(vehicle_type,model,year)
            self.available = True
        else:
            raise Exception('Only up to two cars can be created')
        
    def calculate_rental_fee(self):
        rental_price_per_day = 1000
        return rental_price_per_day * self.days
         
class Motorcycle(Vehicle):
    num_motorcycle = 0
    
    def __init__(self,vehicle_type,model,year,rental_price_per_day,available):
        Motorcycle.num_motorcycle += 1
        if Motorcycle.num_motorcycle <= 2:
            super().__init__(vehicle_type,model,year,rental_price_per_day,available)
            self.available = True
        else:
            raise Exception('Only two motorcycle can be rented at a time')
        
    def calculate_rental_fee(self):
        rental_price_per_day = 600
        return rental_price_per_day * self.days
        

# Testing Car Class
my_car1= Car('Car','Toyota',2015)
my_car2= Car('Car','Mustang',2018)
# my_car3= Car('Car','BMW',2018)      #  This should give an exception because there are only 2 Cars allowed
print(my_car1.rent(2))
print(my_car1.calculate_rental_fee())
print(my_car2.rent(7))
print(my_car1.return_vehicle())
print(my_car1.rent(1))
        

        