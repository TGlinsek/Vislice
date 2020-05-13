import model

def izpis_igre(igra):
    tekst = (
        "Število preostalih poskusov: {stevilo_preostalih_poskusov} \n\n"
        "   {pravilni_del_gesla}    \n\n"
        "Neuspeli poskusi: {neuspeli_poskusi}\n\n"
    ).format(
        stevilo_preostalih_poskusov=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla=igra.pravilni_del_gesla(),
        neuspeli_poskusi=igra.nepravilni_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        "\n########## Juhej, zmaga! Geslo je bilo: {geslo} #########\n\n"
    ).format(
        geslo=igra.pravilni_del_gesla()
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        "Booo, poraz! Geslo je bilo: {geslo} \n\n"
    ).format(
        geslo=igra.geslo
    )
    return tekst

def zahtevaj_vnos():
    crka = input("Zahtevam črko!")
    return crka

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        # najprej izpišemo stanje, da vidimo koliko črk je ipd.
        print(izpis_igre(igra))
        # čakamo na črko od uporabnika
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break
    return  # vrnili smo None. V resnic ne rabmo tega pisat (je pa estetsko, da se vid da je konc funkcije)

# Zaženi igro:
pozeni_vmesnik()