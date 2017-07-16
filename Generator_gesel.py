
import random
import tkinter as tk


#class Geslo:
#    
#    def __init__(self, dolzina_gesla, vrsta_zapisa):
#        self.dolzina_gesla = dolzina_gesla
#        self.vrsta_zapisa = vrsta_zapisa
#        
#    def __repr__(self):
#        return "Geslo dolžine {} v zapisu {}.".format(self.dolzina_gesla, self.vrsta_zapisa,)
#        
#    def zacni(self):
#        self.dolzina_gesla = self.pridobi_dolzino_gesla()
#        self.vrsta_zapisa = self.pridobi_vrsto_zapisa()
#                
#    def pridobi_dolzino_gesla(self):
#        return int(input("Koliko znakov naj vsebuje geslo? "))
#
#    def pridobi_vrsto_zapisa(self):
#        return int(input("Ali bi rad geslo iz cifer (0), iz malih črk (1), iz mešanih črk (2) ali mešanih znakov (3)?"))
#     
#
#############################################################################################
#        
#    def generiraj_nakljucni_znak(self):
#        if self.vrsta_zapisa == 0:
#        elif self.vrsta_zapisa == 1:
#            return random.choice("abcdefghijklmnopqrstuvwxwz")
#        elif self.vrsta_zapisa == 2:
#            return random.choice("abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ")
#        elif self.vrsta_zapisa == 3:
#            return random.choice("0123456789abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ")
#
#    def doloci_geslo(self, dolzina_gesla, vrsta_zapisa):
#        sestavljanje_gesla = []
#        for i in range(len(dolzina_gesla)):
#            simbol = generiraj_nakljucni_znak(d)
#            sestavljanje_gesla.append(simbol)
#        return sestavljanje_gesla
#
#
##############################################################################################
#
#
#d = Geslo(None, None)
#d.zacni()
#d = Geslo(d.dolzina_gesla, d.vrsta_zapisa)
#
#print (d.doloci_geslo)



def nakljucno_geslo(dolzina,zapis):
    geslo = []
    for i in range(dolzina):
    
        if zapis == 0:
                i = random.choice("0123456789")
        elif zapis == 1:
                i = random.choice("abcdefghijklmnopqrstuvwxwz")
        elif zapis == 2:
                i = random.choice("abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif zapis == 3:
                i = random.choice("0123456789abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ")
           
        geslo.append(i)
    return "".join(geslo)



def program():

    zelja = input("Kaj želiš (geslo)?" + "\n").lower()   
    if zelja == "geslo":
        
        dolz = int(input("Koliko znakov naj vsebuje geslo? " + "\n"))
        if dolz < 4 or dolz > 128:
            print ("Napaka. Geslo mora vsebovati med 4 in 128 znakov." + "\n")
            program()
            
        kodir = int(input("V katerem zapisu želiš geslo (0- cifre, 1- male črke, 2- mešane črke, 3- poljubno)? " + "\n"))
        if kodir != 0 and kodir != 1 and kodir != 2 and kodir != 3:
            print ("Napaka. Izbran mora biti način zapisa 0, 1, 2 ali 3." + "\n")
            program()

#    elif zelja == "več gesel":
#        koliko = int(input("Koliko gesel želiš?" + "\n"))
#        if koliko < 2 or koliko > 10:
#            print ("Napaka. Izbrano število generiranih gesel mora biti med 2 in 10." + "\n")
#            program()
#            
#        dolz = int(input("Koliko znakov naj vsebuje geslo? " + "\n"))
#        if dolz < 4 or dolz > 128:
#            print ("Napaka. Geslo mora vsebovati med 4 in 128 znakov." + "\n")
#            program()
#            
#        kodir = int(input("V katerem zapisu želiš geslo (0- cifre, 1- male črke, 2- mešane črke, 3- poljubno)? " + "\n"))
#        if kodir != 0 and kodir != 1 and kodir != 2 and kodir != 3:
#            print ("Napaka. Izbran mora biti način zapisa 0, 1, 2 ali 3." + "\n")
#            program()
        
        
            
        print ("\n" + nakljucno_geslo(dolz, kodir)+ "\n")
        if kodir == 0:
            print (round((10 ** dolz/(2*1000000000)/(3600*24)),1), "dni minimum Hack time per 1000 million/s" + "\n")
        elif kodir == 1:
            print (round((26 ** dolz/(2*1000000000)/(3600*24)),1), "dni minimum Hack time per 1000 million/s" + "\n")
        elif kodir == 2:
            print (round((52 ** dolz/(2*1000000000)/(3600*24)),1), "dni minimum Hack time per 1000 million/s" + "\n")
        elif kodir == 3:
            print (round((62 ** dolz/(2*1000000000)/(3600*24)),1), "dni minimum Hack time per 1000 million/s" + "\n")
        #program()
    else:
        print ("Napaka." + "\n")
        program()

        
def generiraj():
    program()


okno = tk.Tk()

zgoraj = tk.Frame(okno)
zgoraj.pack()
spodaj = tk.Frame(okno)
spodaj.pack()
zapis0 = tk.Button(zgoraj, text = "Samo cifre").grid(row=0, column=0)
zapis1 = tk.Button(zgoraj, text = "Male črke").grid(row=0, column=1)
zapis2 = tk.Button(zgoraj, text = "Mešane črke").grid(row=0, column=2)
zapis3 = tk.Button(zgoraj, text = "Mešane črke + cifre").grid(row=0, column=3)

gumb_generiraj = tk.Button(okno, text = "Generiraj geslo", command = generiraj).pack()





#program()










    
    







    






