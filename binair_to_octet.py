__author__ = "<828'121>, <Yao>"


def binaire_en_octet(chaine_binaire):
    while len(chaine_binaire) % 8 != 0:
        chaine_binaire = '0' + chaine_binaire  # Ajouter des zéros à gauche pour s'assurer que la longueur est un multiple de 8

    octets = [chaine_binaire[i:i+8] for i in range(0, len(chaine_binaire), 8)]
    octets_en_decimal = [int(octet, 2) for octet in octets]
    octets_en_hexadecimal = [hex(decimal)[2:].upper().zfill(2) for decimal in octets_en_decimal]

    return octets_en_hexadecimal

