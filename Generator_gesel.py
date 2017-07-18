import random
import tkinter as tk


########################################################



def nakljucno_geslo_tk(trenutna_dolzina,zapis_tk):
    geslo = []
    for i in range(trenutna_dolzina):
    
        if zapis_tk == 0:
                i = random.choice("0123456789")
        elif zapis_tk == 1:
                i = random.choice("abcdefghijklmnopqrstuvwxwz")
        elif zapis_tk == 2:
                i = random.choice("abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif zapis_tk == 3:
                i = random.choice("0123456789abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ")
           
        geslo.append(i)
    return "".join(geslo)




def program_tk():
    

    dolz_tk = trenutna_dolzina
    kodir_tk = zapis_tk 
                        
    global generirano_geslo
    generirano_geslo = nakljucno_geslo_tk(dolz_tk, kodir_tk)
    
    global hack_time
    #print (generirano_geslo)
    
    
    if kodir_tk == 0:
        hack_time = round((10 ** dolz_tk/(2*1000000000)/(3600*24)),1)
        pass
            
    elif kodir_tk == 1:
        hack_time = round((26 ** dolz_tk/(2*1000000000)/(3600*24)),1)
        pass
            
    elif kodir_tk == 2:
        hack_time = round((52 ** dolz_tk/(2*1000000000)/(3600*24)),1)
        pass
            
    elif kodir_tk == 3:
        hack_time = round((62 ** dolz_tk/(2*1000000000)/(3600*24)),1)
        pass
    
    if hack_time < 1000:
        varnost_gesla_cca = "šibka"
    else:
        if hack_time < 10000:
            varnost_gesla_cca = "zadostna"
        else:
            if hack_time < 100000:
                varnost_gesla_cca = "dobra"
            else:
                if hack_time < 1000000:
                    varnost_gesla_cca = "zelo dobra"
                else:
                    varnost_gesla_cca = "odlična"
                

####################################################



trenutna_dolzina = 8

def osvezi_prikaz():
    prikaz_dolzine["text"] = str(trenutna_dolzina)  

def povecaj_dolzino():
    global trenutna_dolzina
    if trenutna_dolzina == 32:
        pass
    else:
        trenutna_dolzina += 1
    osvezi_prikaz()

def zmanjsaj_dolzino():
    global trenutna_dolzina
    if trenutna_dolzina == 4:
        pass
    else:
        trenutna_dolzina -= 1
    osvezi_prikaz()

    

zapis_tk = 3
    
def zapis_tk0():
    global zapis_tk
    zapis_tk = 0
    osvezi_prikaz_zapisa()

def zapis_tk1():
    global zapis_tk
    zapis_tk = 1
    osvezi_prikaz_zapisa()

def zapis_tk2():
    global zapis_tk
    zapis_tk = 2
    osvezi_prikaz_zapisa()

def zapis_tk3():
    global zapis_tk
    zapis_tk = 3
    osvezi_prikaz_zapisa()  

def osvezi_prikaz_zapisa():
    kateri_zapis["text"] = str(zapis_tk)



generirano_geslo = "Za geslo pritisni na zgornji gumb."

def osvezi_geslo():
    izpis["text"] = str(generirano_geslo)

def novo_geslo_tk():
    program_tk()
    global generirano_geslo
    osvezi_geslo()



varno_geslo = "?"

def osvezi_varnost():
    prikaz_varnosti_gesla["text"] = str(varno_geslo)

def nova_varnost():
    global varno_geslo
    varno_geslo = str(kalkulator_varnosti())
    osvezi_varnost()
    

def kalkulator_varnosti():
    global trenutna_dolzina
    global hack_time
    global zapis_tk
    
    if zapis_tk == 0:
        hack_time = round((10 ** trenutna_dolzina/(2*1000000000)/(3600*24)),1)
        pass
            
    elif zapis_tk == 1:
        hack_time = round((26 ** trenutna_dolzina/(2*1000000000)/(3600*24)),1)
        pass
            
    elif zapis_tk == 2:
        hack_time = round((52 ** trenutna_dolzina/(2*1000000000)/(3600*24)),1)
        pass
            
    elif zapis_tk == 3:
        hack_time = round((62 ** trenutna_dolzina/(2*1000000000)/(3600*24)),1)
        pass
    
    if hack_time < 1000:
        return "šibka"
    else:
        if hack_time < 10000:
            return "zadostna"
        else:
            if hack_time < 100000:
                return "dobra"
            else:
                if hack_time < 1000000:
                    return "zelo dobra"
                else:
                    return "odlična"


###########################################


okno = tk.Tk()

naslov = tk.Frame(okno)
naslov.pack()

preglednost0 = tk.Label(okno)
preglednost0.pack()

izbor_zapisa = tk.Frame(okno)
izbor_zapisa.pack()

kateri_zapis = tk.Label(okno, font = ("TkDefaultFont", 12), bg = "white")
kateri_zapis.pack()
osvezi_prikaz_zapisa()

preglednost1 = tk.Label(okno)
preglednost1.pack()

stevilo_znakov = tk.Frame(okno)
stevilo_znakov.pack()

prikaz_dolzine = tk.Label(okno, font = ("TkDefaultFont", 12), bg = "white")
prikaz_dolzine.pack()
osvezi_prikaz()

preglednost2 = tk.Label(okno)
preglednost2.pack()

spodaj = tk.Frame(okno)
spodaj.pack()

izpis = tk.Label(okno, bg = "white", font = ("Courier", 16))
izpis.pack()
osvezi_geslo()

preglednost3 = tk.Label(okno)
preglednost3.pack()

spodaj2 = tk.Frame(okno)
spodaj2.pack()



prikaz_varnosti_gesla = tk.Label(okno, font = ("TkDefaultFont", 12), fg = "blue")
prikaz_varnosti_gesla.pack()
osvezi_varnost()



zapis_naslova = tk.Label(naslov, font = ("TkDefaultFont", 13), text = "Nastavite željene vrednosti:").pack()

zapis0 = tk.Button(izbor_zapisa, font = ("TkDefaultFont", 11), text = "Samo cifre", command=zapis_tk0).grid(row=0, column=0)
zapis1 = tk.Button(izbor_zapisa, font = ("TkDefaultFont", 11), text = "Male črke", command=zapis_tk1).grid(row=0, column=1)
zapis2 = tk.Button(izbor_zapisa, font = ("TkDefaultFont", 11), text = "Mešane črke", command=zapis_tk2).grid(row=0, column=2)
zapis3 = tk.Button(izbor_zapisa, font = ("TkDefaultFont", 11), text = "Mešane črke + cifre", command=zapis_tk3).grid(row=0, column=3)

zapis_za_dolzino = tk.Label(stevilo_znakov, font = ("TkDefaultFont", 11), text = "Število znakov:  ").grid(row=0, column=0)
plus_gumb = tk.Button(stevilo_znakov, font = ("TkDefaultFont", 11), text = "+", command=povecaj_dolzino).grid(row=0, column=1)
minus_gumb = tk.Button(stevilo_znakov, font = ("TkDefaultFont", 11), text = "-", command=zmanjsaj_dolzino).grid(row=0, column=2)

gumb_generiraj = tk.Button(spodaj, font = ("TkDefaultFont", 13), text = "Generiraj geslo", command = novo_geslo_tk).pack()


gumb_varnost = tk.Button(spodaj2, font = ("TkDefaultFont", 11), text = "Varnost", command = nova_varnost).pack()















    
    







    






