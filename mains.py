# import datetime
# import datetime

# class MyAge:
#     def __init__(self, year):
#         self.year = year
    
#     def __call__(self):
#         cur = datetime.datetime.now().year
#         age = cur - self.year  # Yoshni hisoblash
#         return f"Yangi yosh: {age}"


# og = MyAge(2000)


# print(og())


# class Beshga:
#     def __init__(self, number):
#         self.number = number
#         self.current = 0  # Iteratsiya qilish uchun boshlang'ich qiymat

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.number:
#             result = self.current * 5
#             self.current += 1
#             return result
#         else:
#             raise StopIteration

# # Ob'yekt yaratamiz
# obj = Beshga(10)

# # Iteratsiya qilamiz
# for inter in obj:
#     print(inter)




# class MyClass:
#      def __init__(self,name):
#           self.name = name
        
    
#      def __setattr__ (self,name,phone):
#          print(f"telfon={name} = {phone}")
#          super().__setattr__(name,phone)
        
        
    

# obj1 = MyClass("ali")

# obj1.manzir = "xadra"
# obj1.phone = 888789473

# print(obj1.manzir,obj1.phone)



# class Number:
#     def __init__(self,age):
#         self.age = age
    
#     def __eq__(self, value):
#         return (self.age == value.age)
        
        
#     def __lt__(self, b):
#         return (self.age < b.age)
        
# num1 = Number(12)
# num2 = Number(20)
# print(num1 == num2)



class MyIterator:
    def __init__(self,max_value):
        self.max = max_value
        self.conut = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.conut <self.max:
            self.conut += 5
            return self.conut
        else:
            raise StopIteration
    
    
obj = MyIterator(10)

for i in obj:
    print(i)