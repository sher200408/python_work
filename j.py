class Mehmon:
    def __init__(self, ism, yosh, xona):
        self.ism = ism
        self.yosh = yosh
        self.xona = xona

    def kirish(self):
        print(f"{self.ism} mehmonxonaga kirdi.")

    def chiqish(self):
        print(f"{self.ism} mehmonxonadan chiqdi.")

    def xona_raqami(self):
        print(f"{self.ism}ning xonasi: {self.xona}")

    def yoshini_korsat(self):
        print(f"{self.ism}ning yoshi: {self.yosh}")
# Mehmon ob'ektini yaratish
mehmon1 = Mehmon("Ali", 30, 101)

# Funksiyalarni chaqirish
mehmon1.kirish()
mehmon1.xona_raqami()
mehmon1.yoshini_korsat()
mehmon1.chiqish()
