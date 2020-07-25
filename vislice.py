import bottle
import model2
import os

# ./views
# c:\\Users\\Tadej\\Documents\\Tekst\\Faks\\UVP\\Vislice\\views
vislice = model2.Vislice()


@bottle.get('/')
def index():
    # relj = os.path.join("UVP\\Vislice\\views", "index2.tpl")
    relj = "UVP\\Vislice\\views\\index2.tpl"
    return bottle.template(relj)


@bottle.post('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre))


@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus1 = vislice.igre[id_igre]
    relativ = os.path.join("UVP\\Vislice\\views", "igra2.tpl")
    return bottle.template(relativ, id_igre=id_igre, igra=igra, poskus=poskus1)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    # igra, poskus = vislice.igre[id_igre]
    crka = bottle.request.forms.getunicode('crka')  # unicode, ker so lahk šumniki tut
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}/'.format(id_igre))


# tuki zdj sam še za sliko poskrbimo

@bottle.get('/img/<picture>')  # tu je lahko / na konc al pa ne
def serve_pictures(picture):
    return bottle.static_file(picture, root="UVP\\Vislice\\img")

bottle.run(reloader=True, debug=True)