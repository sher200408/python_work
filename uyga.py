class Hayvonlar:
    def __init__(self,name,rangi,yoshi):
        self.name = name
        self.rangi = rangi
        self.yoshi = yoshi
        
    def atribut(self,attr_name,value):
        setattr(self,attr_name,value)
        
obyekt1 = Hayvonlar("leo","sariq",5)
obyekt2 = Hayvonlar("tiger","to'q sariq",10)
obyekt3 = Hayvonlar("qoplon","qora",2)
obyekt4 = Hayvonlar("fil","ko'k",4)
obyekt5 = Hayvonlar("ot","qora",15)

obyekt1.atribut("sherni yoshi",6)
obyekt2.atribut("tiger yoshi",11)
obyekt3.atribut("qoplon yoshi",3)
obyekt4.atribut("fil yoshi",8)
obyekt5.atribut("otni yoshi","oldi enid")

import datetime
class Car:
    def __init__(self,name,modir,yil):
        self.name = name
        self.modir = modir
        self.yil = yil
    
    def __call__(self,value):
        self.yil += value

    def get_age(self):
        s = datetime.datetime.now().year
        return s - self.yil

car1 = Car("Bwm","M5 f90",2019)
car2 = Car("Bwm","M5 f90",2020)

cars1 = car1.get_age()
cars2 = car2.get_age()

print(cars1,cars2)