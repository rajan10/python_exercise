class Driver:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return f"{self.name} is the drivername"
        
class Car:
    def __init__(self,make,model):
        self.make=make
        self.model= model
        self.driver=None
    def __str__(self):
        return f"{self.driver} is the name of driver"
             
driver1=Driver("Rajan")
print(driver1)
car1=Car("Toyota","Camry")
print(car1)
car1.driver=driver1
print(car1.driver)
