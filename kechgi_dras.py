# __repr__ — Obyektning texnik ko'rinishi (dasturchi uchun)
# Bu metod obyektni repr() funksiyasiga berilganda qanday ko'rinishda
# chiqishini belgilaydi. U odatda obyektning texnik ko'rinishini beradi va dasturchi
# tomonidan tushunarli bo'lishi kerak. Agar __str__ metodini belgilamagan bo'lsangiz,
# print() metodi ham __repr__ ni chaqiradi.

# class MyClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         `

#     def __repr__(self):
#         return f"MyClass(name='{self.name}', age={self.age})"

#     def __str__(self):
#         pass


# obj = MyClass("Alice", 30)
# print(repr(obj))  # MyClass(name='Alice', age=30)

# __del__ — Obyektni o'chirish (Destructor)
# __del__ — obyekt o'chirilganda yoki xotiradan yo'q qilinishi kerak
# bo'lganda chaqiriladigan metoddir. Biroq, bu metoddan foydalanishda
# ehtiyot bo'lish kerak


# class MyClass:
#     def __del__(self):
#         print(f"Obyekt o'chirildi: {self}")

# obj = MyClass()
# del obj


# __enter__ va __exit__ — Context Managerlar bilan ishlash
# Bu metodlar obyektlarni context manager sifatida ishlatishga imkon beradi
# (masalan, with iborasi orqali). __enter__ resurslarni ochish,
# __exit__ esa resurslarni yopish uchun ishlatiladi.

# class MyContextManager:
#     def __enter__(self):
#         print("Kontekst boshlandi")
#         file = open("file1.txt","r")
#         file.write()
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Kontekst tugadi")


# with MyContextManager():
#     print("Kontekst ichida")

# __call__ — Obyektni funksiya kabi chaqirish

# class MyCallableClass:
#     def __init__(self, value):
#         self.value = value

#     def __call__(self, increment):
#         self.value += increment
#         print(f"Yangi qiymat: {self.value}")
# #
# #
# obj = MyCallableClass(10)
# obj(5)  # Yangi qiymat: 15

# __iter__ va __next__ — Iteratorlar
# Bu metodlar obyektlarni iterator sifatida ishlatishga imkon beradi.
# __iter__ iteratorda boshlang'ich holatni o'rnatadi, __next__ esa keyingi elementni qaytaradi.


# class MyIterator:
#     def __init__(self, max_value):
#         self.max_value = max_value
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.max_value:
#             self.current += 5
#             return self.current
#         else:
#             raise StopIteration


# obj = MyIterator(5)
# for value in obj:
#     print(value)


# __contains__ — in operatori bilan ishlash
# __contains__ metodi in operatori ishlatilganda
# chaqiriladi va ob'ekt ichida element mavjudligini tekshiradi.

# class MyList:
#     def __init__(self, s):
#         self.s = s

#     def __contains__(self, a):
#         return a in self.s
# #
# #
# obj = MyList([1, 2, 3, 4])
# print(3 in obj)  # True
# print(5 in obj)  # False

#  __setattr__, __getattr__, __delattr__ — Attribute'larni boshqarish
# Bu metodlar obyekt ichidagi attribute'lar bilan ishlashda qo'llaniladi.

# __setattr__ — attribute'ga qiymat o'rnatishda chaqiriladi.
# __getattr__ — attribute'ga kirishda chaqiriladi (agar attribute mavjud bo'lmasa).
# __delattr__ — attribute'ni o'chirishda chaqiriladi.


# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def __setattr__(self, name, value):
#         print(f"Attribute o'rnatilmoqda: {name} = {value}")
#         super().__setattr__(name, value)

#     def __getattr__(self, name):
#         print(f"Attribute topilmadi: {name}")
#         return None



# obj = MyClass("Alice")
# obj.age = 30  # Attribute o'rnatilmoqda: age = 30
# # print(obj.age)  # 30
# print(obj.name, "NAME ====")
# print(obj.age, "Age ====")

# obj1 = MyClass('ali')
# obj1.phone = 998901104545
# obj1.manzil = "Xadra"
# print(obj1.phone,obj1.manzil)
# print(obj1.yoshi)



#  __eq__, __ne__, __lt__, __gt__, __le__, __ge__ — Taqqoslash operatorlari
# Bu metodlar obyektlarni taqqoslash uchun ishlatiladi:

# __eq__ — tenglik (==).
# __ne__ — teng emas (!=).
# __lt__ — kichik (<).
# __le__ — kichik yoki teng (<=).
# __gt__ — katta (>).
# __ge__ — katta yoki teng (>=).


# class MyNumber:
#     def __init__(self, value):
#         self.value = value

#     def __eq__(self, other):
#         return self.value == other.value

#     def __lt__(self, other):
#         return self.value < other.value


# num1 = MyNumber(10)
# num2 = MyNumber(20)

# print(num1 == num2)  # False
# print(num1 < num2)  # True