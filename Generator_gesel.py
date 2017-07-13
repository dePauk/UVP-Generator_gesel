import random


class Geslo:
    
    def __init__(self, dolzina_gesla, vrsta_zapisa):
        self.dolzina_gesla = dolzina_gesla
        self.vrsta_zapisa = vrsta_zapisa
        
    def __repr__(self):
        return "Geslo dolžine {} v zapisu {}.".format(self.dolzina_gesla, self.vrsta_zapisa,)
        
    def zacni(self):
        self.dolzina_gesla = self.pridobi_dolzino_gesla()
        self.vrsta_zapisa = self.pridobi_vrsto_zapisa()
                
    def pridobi_dolzino_gesla(self):
        return int(input("Koliko znakov naj vsebuje geslo? "))

    def pridobi_vrsto_zapisa(self):
        return int(input("Ali bi rad geslo iz cifer (0), iz malih črk (1), iz mešanih črk (2) ali mešanih znakov (3)?"))
     

#############################################################################################
        
    def generiraj_nakljucni_znak(self):
        if self.vrsta_zapisa == 0:
            return random.randint[0,9]
        if self.vrsta_zapisa == 1:
            return random.choice("abcdefghijklmnopqrstuvwxwz")
        if self.vrsta_zapisa == 2:
            return random.choice("abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if self.vrsta_zapisa == 3:
            return random.choice("0123456789abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def doloci_geslo(self, dolzina_gesla, vrsta_zapisa):
        sestavljanje_gesla = []
        for i in range(len(dolzina_gesla)):
            simbol = generiraj_nakljucni_znak(d)
            sestavljanje_gesla.append(simbol)
        return sestavljanje_gesla


##############################################################################################



d = Geslo(None, None)
d.zacni()
d = Geslo(d.dolzina_gesla, d.vrsta_zapisa)

#print (d.doloci_geslo)







