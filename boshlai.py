class Dom():
    """ eta class dom uyda """
    def __init__(self,name):
        self.name = name
    
    def build(self):
        print(f"uy nomli {self.name}bor")
    
    
hoter1 = Dom("kochada")
hoter2 = Dom("tolab toral")

hoter1.build()
hoter2.build()
        
