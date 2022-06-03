#class object attribute
class SuperMan:
  or_name = "Super Man"
  def __init__(self,name,age):
    self.name = name
    self.age = age
    
def run(self):
    print("Yes he can run")
    
supermanObj = SuperMan("Gogo",24)
print(SuperMan.or_name)  
print(SuperMan.__name__)


#Encapsulation - data hiding
print("helllo".capitalize()) 

 
#class Method and static method
class Player:
    def __init__(self,name,age):
        self.age = age
        self.name = name
        
    @classmethod
    def player_age(cls,num1,num2):
        return num1 + num2
p1 = Player("Neeti",24)
print(p1.player_age(10,14))  

class Player:
    def __init__(self,name,age):
        self.age = age
        self.name = name
        
    @classmethod
    def player_age(cls,num1,num2):
        return cls("neeti",num1 + num2)
p1 = Player("Neeti",24)

print(p1.player_age(10,14)) 
print(p1.name) 
print(p1.age)
  
#static method called by class name  
class Player:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @staticmethod
    def player_age(num1 ,num2):
        return num1 + num2
print(Player.player_age(10,20))                       
    
    
    
#inheritance:
class Father:
    car = 2
    def home(self):
        return "Father has 3 home"
        
class Son(Father):
    pass

s1 = Son()
f1 = Father()
print(s1.home()) 
print(s1.car)           

print(f1.home()) 
print(f1.car) 


#Abstract class
from abc import ABC,abstractclassmethod
class Father(ABC):
    car = 2
    def home(self):
        return "Father has 3 home"
        
class Son(Father):
    pass

s1 = Son()
f1 = Father()
print(s1.home()) 
print(s1.car)           

print(f1.home()) 
print(f1.car) 


