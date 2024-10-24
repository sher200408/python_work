import re
import json
import os


class Talaba:
    def __init__(self, ism, telefon, student_id, kurs):
        self.ism = self.ism_setter(ism)
        self.telefon = self.telefon_setter(telefon)
        self.id = student_id
        self.kurs = kurs

    @staticmethod
    def telefon_setter(telefon):  # 'self' o'rniga 'telefon' bo'lishi kerak
        regex = r"^\+?[0-9]{9,15}$"
        if re.match(regex, telefon):
            return telefon
        else:
            raise ValueError("Noto'g'ri telefon raqami. Telefon raqami + bilan boshlanishi mumkin va 9-15 raqamdan iborat bo'lishi kerak.")

    def to_dict(self):
        return self.__dict__


def talaba_yarat():
    while True:
        try:
            ism = input("Ismingizni kiriting: ")
            telefon = input("Telefon raqamingizni kiriting: ")
            student_id = input("ID kiriting: ")
            kurs = input("Kursni kiriting: ")

            return Talaba(ism, telefon, student_id, kurs)
        except ValueError as e:
            print(e)


def write_to_json(talaba):
    if not os.path.exists('students.json'):
        with open('students.json', 'w') as file:
            json.dump([], file)

    with open('students.json', 'r+') as file:
        data = json.load(file)
        data.append(talaba.to_dict())
        file.seek(0)
        json.dump(data, file, indent=4)


def main():
    while True:
        talaba = talaba_yarat()
        write_to_json(talaba)
        print("Talaba qo'shildi.")

main()
