class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=f'{self.year} {self.odometer_reading} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'this car has {self.odometer_reading} miles on it')

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading :
            self.odometer_reading=mileage
        else:
            print(" you can't roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery:
    def __init__(self,batter_size=75):
        self.batter_size=batter_size
    def decribe_battery(self):
        print(f'this car has a {self.battery_size}-kwh battery')
    def upgrade_battery(self):
        if self.batter_size!=100:self.batter_size=100
    def get_range(self):
        if self.batter_size==75:range=260
        else:range=315
        print(f'this car can go about {range} miles on a full charge.')

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

test=ElectricCar('tesla','model s',2019)
test.battery.get_range()
test.battery.upgrade_battery()
test.battery.get_range()


