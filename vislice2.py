import bottle
import model2
import os

# vse vrstice, kjer piše kej v zvezi s cookiji, so pač na novo. Ostalo kar je, smo id_igre odstranli povečini
SKRIVNOST = "moja_prva_skrivnost"
DATOTEKA_S_STANJEM = "UVP\\Vislice\\stanje.json"
DATOTEKA_Z_BESEDAMI = "UVP\\Vislice\\besede.txt"  # mi bomo vzeli kar vse slo besede, ampak lahk bi karkol

# ./views
# c:\\Users\\Tadej\\Documents\\Tekst\\Faks\\UVP\\Vislice\\views
vislice = model2.Vislice(DATOTEKA_S_STANJEM, DATOTEKA_Z_BESEDAMI)
vislice.nalozi_igre_iz_datoteke()  # seveda moramo spet naložiti to igro

@bottle.get('/')
def index():
    # relj = os.path.join("UVP\\Vislice\\views", "index2.tpl")
    relj = "UVP\\Vislice\\views\\index2.tpl"
    return bottle.template(relj)


# vaje spletni vmesnik
@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()

    # tu moramo pretvorit v string (v lepem formatu)
    bottle.response.set_cookie('idigre', "id_igre{}".format(id_igre), secret="SKRIVNOST", path='/')  # response ma set cookie, request pa get cookie
    bottle.redirect('/igra/')



# iz prejšnjih vaj
"""
@bottle.post('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre))


@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus1 = vislice.igre[id_igre]
    relativ = os.path.join("UVP\\Vislice\\views", "igra2.tpl")
    return bottle.template(relativ, id_igre=id_igre, igra=igra, poskus=poskus1)
"""
@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('idigre', secret="SKRIVNOST").split("e")[1])  # zgoraj smo uporabili format, oblike idigre5, recimo. Zato smo pri e splittal in vzeli sam številko
    igra, poskus1 = vislice.igre[id_igre]
    relativ = os.path.join("UVP\\Vislice\\views", "igra2.tpl")
    return bottle.template(relativ, igra=igra, poskus=poskus1)

# @bottle.post('/igra/<id_igre:int>/')
@bottle.post('/igra/')
def ugibaj():
    # igra, poskus = vislice.igre[id_igre]
    id_igre = int(bottle.request.get_cookie('idigre', secret="SKRIVNOST").split("e")[1])
    crka = bottle.request.forms.getunicode('crka')  # unicode, ker so lahk šumniki tut
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')


# tuki zdj sam še za sliko poskrbimo

@bottle.get('/img/<picture>')  # tu je lahko / na konc al pa ne
def serve_pictures(picture):
    return bottle.static_file(picture, root="UVP\\Vislice\\img")

bottle.run(reloader=True, debug=True)