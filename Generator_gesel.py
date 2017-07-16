import random
import tkinter as tk





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

                        
        print ("\n" + nakljucno_geslo(dolz, kodir)+ "\n")
        if kodir == 0:
            print (round((10 ** dolz/(2*1000000000)/(3600*24)),1), "dni minimum Hack time per 1000 million/s" + "\n")
        elif kodir == 1:
            print (round((26 ** dolz/(2*1000000000)/(3600*24)),1), "dni minimum Hack time per 1000 million/s" + "\n")
        elif kodir == 2:
            print (round((52 ** dolz/(2*1000000000)/(3600*24)),1), "dni minimum Hack time per 1000 million/s" + "\n")
        elif kodir == 3:
            print (round((62 ** dolz/(2*1000000000)/(3600*24)),1), "dni minimum Hack time per 1000 million/s" + "\n")
#        program()
#    else:
#        print ("Napaka." + "\n")
#        program()

        
def generiraj():
    program()



trenutna_dolzina = 8

def osvezi_prikaz():
    prikaz_dolzine["text"] = str(trenutna_dolzina)
    

def povecaj_dolzino():
    global trenutna_dolzina
    trenutna_dolzina += 1
    osvezi_prikaz()

def zmanjsaj_dolzino():
    global trenutna_dolzina
    trenutna_dolzina -= 1
    osvezi_prikaz()
    
    


okno = tk.Tk()

naslov = tk.Frame(okno)
naslov.pack()

izbor_zapisa = tk.Frame(okno)
izbor_zapisa.pack()

stevilo_znakov = tk.Frame(okno)
stevilo_znakov.pack()

prikaz_dolzine = tk.Label(okno)
prikaz_dolzine.pack()
osvezi_prikaz()

spodaj = tk.Frame(okno)
spodaj.pack()

izpis = tk.Frame()
izpis.pack()


zapis_naslova = tk.Label(naslov, text = "Nastavite željene vrednosti:").pack()

zapis0 = tk.Button(izbor_zapisa, text = "Samo cifre").grid(row=0, column=0)
zapis1 = tk.Button(izbor_zapisa, text = "Male črke").grid(row=0, column=1)
zapis2 = tk.Button(izbor_zapisa, text = "Mešane črke").grid(row=0, column=2)
zapis3 = tk.Button(izbor_zapisa, text = "Mešane črke + cifre").grid(row=0, column=3)

zapis_za_dolzino = tk.Label(stevilo_znakov, text = "Število znakov:  ").grid(row=0, column=0)
plus_gumb = tk.Button(stevilo_znakov, text = "+", command=povecaj_dolzino).grid(row=0, column=1)
minus_gumb = tk.Button(stevilo_znakov, text = "-", command=zmanjsaj_dolzino).grid(row=0, column=2)

gumb_generiraj = tk.Button(spodaj, text = "Generiraj geslo", command = generiraj).pack()

izpis_gesla = tk.Label(izpis, text = "Še ne deluje. LP").pack()



#program()










    
    







    






