class hayvonlar:
    def __init__(self, name, species, age, color, weight):
        self.name = name
        self.species = species
        self.age = age
        self.color = color
        self.weight = weight

    def update_hayvonlar(self, attr_name, value):
        setattr(self, attr_name, value)


animal1 = hayvonlar("Leo", "Sher", 5, "Sariq", 190)
animal2 = hayvonlar("Tiger", "Yo'lbars", 3, "To'q sariq", 220)
animal3 = hayvonlar("Bunny", "Quyon", 2, "Oq", 1.5)
animal4 = hayvonlar("Eagle", "Burgut", 4, "Qora", 7.0)
animal5 = hayvonlar("Cheetah", "Yozqon", 6, "To'q kulrang", 50)
""" 1chi hayoni sher eniga uzun"""
animal1.update_hayvonlar("weight", 195)
"""2chi hayon tigerni rangi """
animal2.update_hayvonlar("color", "Qora va oq")
"""3chi hayon yoshiga kuchiq"""
animal3.update_hayvonlar("age", 3)
"""4chi hayon turlari burgut"""
animal4.update_hayvonlar("species", "burgut")
"""5chi hayon ismli hayoncha chita """
animal5.update_hayvonlar("name", "Chita")



import datetime
class Car:
    def __init__(self, model, yil):
        self.model = model
        self.yil = yil

    def update_year(self, value):
        self.yil += value  

    def get_age(self):
        current_year = datetime.datetime.now().year
        return(  current_year - self.yil  )

car1 = Car("Chevrolet nexia 3", 2018)

car2 = Car("BYD xan", 2020)

car3 = Car("BYD song puls", 2017)

car4 = Car("Chevrolet matiz", 2019)

car5 = Car("BMW X5", 2021)



car_age1 = car1.get_age()
print(f" {car1.model} avtomabili yoshi: {car_age1} yil")


car_age2 = car2.get_age()
print(f" {car2.model} avtomabili yoshi: {car_age2} yil")



car_age3 = car3.get_age()
print(f" {car3.model} avtomabili yoshi: {car_age3} yil")



car_age4 = car4.get_age()
print(f" {car4.model} avtomabili yoshi: {car_age4} yil")




car_age5 = car5.get_age()
print(f" {car5.model} avtomabil yoshi: {car_age5} yil")

