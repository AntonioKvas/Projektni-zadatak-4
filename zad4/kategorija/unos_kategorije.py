from artikl import unos_artikla
from utilities import unos_cijelog_pozitivnog_broja
def unos_kategorije(redni_broj):
    kategorija = {}
    kategorija['naziv'] = input(f'Unesite naziv {redni_broj}. kategorije: ')
    kategorija['artikli'] = []

    br_artikala = unos_cijelog_pozitivnog_broja(f'Unesite broj artikala za {redni_broj}. kategoriju: ')
    for i in range(1, br_artikala + 1):
        kategorija['artikli'].append(unos_artikla(i))

    return kategorija

