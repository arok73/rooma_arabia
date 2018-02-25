# Roomalaisten numeroiden muunnin - Ari Oksanen 

# funktio kokonaisluvun muuntamiseksi roomalaisiksi luvuiksi
def arabiasta_roomaan(numero):
    numero_tuple = ((1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'),
                   (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M'))
    roomalainen_luku = ''
    
    # Iteroidaan numero_tuple läpi käänteisessä järjestyksessä kunnes syötetty numero on yhtä suuri kuin arvo tuplessa. 
    # Arvoa vastaava merkki sijoitetaan roomalainen_luku muuttujaan ja luku-muuttujasta vähennetään arvo-muuttuja.
    # Jatketaan kunnes numero-muuttuja on 0. 
    # Lopuksi palautetaan string-tyyppinen arvo tulostettavaksi
    while numero > 0:
        for arvo, merkki in reversed(numero_tuple):
            while numero >= arvo:
                roomalainen_luku += merkki
                numero -= arvo
    return roomalainen_luku

# funktio roomalaisen luvun muuntamiseksi kokonaisluvuksi
def roomasta_arabiaan(roomalainen_syote):
    rooma_tuple = (('I', 1), ('IV', 4), ('V', 5), ('IX', 9), ('X', 10), ('XL', 40), ('L', 50), ('XC', 90), ('C', 100),
                  ('CD', 400), ('D', 500), ('CM', 900), ('M', 1000))
    palautettava_luku = 0

    # Iteroidaan rooma_tuple läpi käänteisessä järjestyksessä, niin kauan kun roomalainen_syote-muuttujan alusta löytyy vastaava merkki.
    # rooma_tuplen merkkiä vastaava arvo sijoitetaan palautettava_luku-muuttujaan ja roomalainen_syote-muuttujan arvosta vähennetään merkin pituus alusta.
    # Mikäli iterointi jatkuu, lisätään seuraavalla kierroksella palutettava_luku-muuttujaan arvo-muuttujan arvo.
    # Lopuksi palautetaan int-tyyppinen luku tulostettavaksi.
    for merkki, arvo in reversed(rooma_tuple):
        while roomalainen_syote.startswith(merkki):
            palautettava_luku += arvo
            roomalainen_syote = roomalainen_syote[len(merkki):]
    return palautettava_luku


if __name__ == '__main__':

    print()
    print("**********************MENU**********************")
    print()
    print("1. Muunna Roomalaiset numerot kokonaisluvuksi")
    print("2. Muunna kokonaisluku Roomalaiseksi numeroksi")
    print()
    menu_valinta = 0
    arabialainen_luku = 0
    sallitut_merkit = set('IVXLCDM')
    sallitut_valinnat = [1, 2]
    while True:
        try:
            while menu_valinta not in sallitut_valinnat:
                menu_valinta = int(input("Anna valintasi: "))
            break
        except ValueError:
            print("Syötä numero 1 tai 2")
    if menu_valinta == 1:
            while True:
                try:
                    while (arabialainen_luku > 3999) or (arabialainen_luku < 1):
                        arabialainen_luku =  int(input("Anna kokonaisluku (1-3999): "))
                    break    
                except ValueError:
                    print("Syötä vain kokonaislukuja! Yritä uudelleen.")

            print("Roomalainen luku: " + arabiasta_roomaan(arabialainen_luku))

    elif menu_valinta == 2: 
        while True:
            roomalainen_luku = input('Anna roomalainen luku (IVXLCDM): ')
            if set(roomalainen_luku).issubset(sallitut_merkit):
                print()
                print("Arabialainen luku: {}".format(roomasta_arabiaan(roomalainen_luku)))
                break
            else:
                print('Syötä vain kirjaimia I,V,X,L,C,D tai M! Yritä uudelleen.')
