import random


class Geslo:
    
    def __init__(self, dolzina_gesla, vrsta_zapisa):
        self.dolzina_gesla = dolzina_gesla
        self.vrsta_zapisa = vrsta_zapisa
        
    def __repr__(self):
        return "Geslo dolžine {} v zapisu {}.".format(self.dolzina_gesla, self.vrsta_zapisa)
        
    def zacni(self):
        self.dolzina_gesla = self.pridobi_dolzino_gesla()
        self.vrsta_zapisa = self.pridobi_vrsto_zapisa()
                
    def pridobi_dolzino_gesla(self):
        return int(input("Koliko znakov naj vsebuje geslo? "))

    def pridobi_vrsto_zapisa(self):
        return int(input("Ali bi rad geslo iz cifer (0), iz malih črk (1), iz mešanih črk (2) ali mešanih znakov (3)"))
    
        


d = Geslo(None, None)
d.zacni()
d = Geslo(d.dolzina_gesla, d.vrsta_zapisa)







