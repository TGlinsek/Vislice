import random

STEVILO_DOVOLJENIH_NAPAK = 9

PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "W"
PORAZ = "X"


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
                if self.zmaga:
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