class Person:
    def __init__(self,pin ,karta):
        self.pin = pin 
        self.karta = karta
        
    def __str__(self):
        return "person digan class"

person1 = Person("8881","1111 2222 3333 4444 5555")
person2 = Person("8882","1112 2223 3333 4444 0000")
person3 = Person("8883","1113 2224 3333 4444 9999")
person4 = Person("8884","1114 2225 3333 4444 1010")
all_person = [person1,person2,person3,person4]
try :
    while True:
        print("odam ma'lumotlar kirish")
        pinme = input("karta pin_code kiriting = ")
        karta = input("karta sss")
        flag = False
        for item_check in all_person:
            if item_check.pin == pinme and  item_check.karta == karta:
                flag = True
                print("-------------------------------")
                print(f"{item_check.pin} ishladi😊 malads to'g'ri kirtingiz")
                print("<---------nonononono------------->")
                break
        if not flag:
            print("-----------------")
            print("xato boldi emas")
            print("---------------")
    
except Exception as e:
    print(f"ishlamdi xato {e} 😫")
