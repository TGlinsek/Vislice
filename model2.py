import random
import json  # to smo spremenil 27.5

STEVILO_DOVOLJENIH_NAPAK = 9

PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "W"
PORAZ = "X"

ZACETEK = "S"

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        if crke is None:
            self.crke = []
        else:
            self.crke = [i.upper() for i in crke]
    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
    
    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        for i in self.geslo:
            if i not in self.crke:
                return False
        return True
    
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        string = ""
        for i in self.geslo:
            if i in self.crke:
                string += i + " "
            else:
                string += "_ "
        return string
    
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            if crka in self.pravilne_crke():
                return PONOVLJENA_CRKA
            else:
                return NAPACNA_CRKA
        else:
            self.crke.append(crka.upper())
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                return NAPACNA_CRKA
    
# ".\\besede.txt" bi lahk tut. To specificira relativno pot
with open("C:\\Users\\Tadej\\Documents\\Tekst\\Faks\\UVP\\Vislice\\besede.txt", "r", encoding="utf-8") as bes:
    bazen_besed = [vrstica.strip().upper() for vrstica in bes]

# igra = Igra("jazz", ["a", "e"])

def nova_igra():
    return Igra(random.choice(bazen_besed))

class Vislice:

    """
    >>> v = Vislice()
    >>> v.nova_igra()
    0
    >>> v.igre
    {1: (<__main__.Igra object at 0x00000133B2328508>, 'S')}
    """

    def __init__(self, datoteka_s_stanjem, datoteka_z_besedami='UVP\\Vislice\\besede.txt'):  # tu smo spremenil 27.5
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_z_besedami = datoteka_z_besedami
    
    def prost_id_igre(self):
        return max(self.igre.keys(), default=-1) + 1  # nov ključ, ki ga zagotovo nobena druga igra še nima
    
    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()

        with open(self.datoteka_z_besedami, 'r', encoding='utf-8') as f:
            bazen_besed = [vrstica.strip().upper() for vrstica in f]  # bazen besed je lah zdj drugačen pr vsaki novi igri

        igra = nova_igra()
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (igra, ZACETEK)

        self.zapisi_igre_v_datoteko()
        return id_igre  # vrne ravnokar zgeneriran ključ

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra, _ = self.igre[id_igre]  # prejšnje stanje nas ne zanima

        poskus = igra.ugibaj(crka)  # to ni ta ista metoda
        self.igre[id_igre] = (igra, poskus)  # shrani nazaj stanje te igre

        self.zapisi_igre_v_datoteko()

    # na novo napisano za vislice2 (delo z datotekami) - tut uzgor smo mal spremenil, ampak nč takega
    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as f:
            igre_1 = {
                id_igre : ((igra.geslo, igra.crke), poskus)  # s tem bomo rekonstruirali
                for id_igre, (igra, poskus) in self.igre.items() # igre.items je slovar, vrednost je nabor (igra, poskus) 
            }
            json.dump(igre_1, f)  # ni self.igre
        return  # ne rabmo dejansko
    
    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding="utf-8") as f:
            igre = json.load(f)
            self.igre = {
                int(id_igre): (Igra(geslo, crke), poskus)  # Igra (z vlko) je en naš class
                for id_igre, ((geslo, crke), poskus) in igre.items()
            }  
    # poleg teh dveh funkcij moramo še nardit neki v spletnemu vmesniku
    # Commenti NISO dovoljeni v JSONu