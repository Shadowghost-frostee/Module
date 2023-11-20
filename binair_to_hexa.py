__author__ = "<828'121>, <Yao>"

def binaire_en_hexadecimal(chaine_binaire):
    while len(chaine_binaire) % 4 != 0:
        chaine_binaire = '0' + chaine_binaire  # Ajouter des zéros à gauche pour s'assurer que la longueur est un multiple de 4

    hexadecimals = [hex(int(chaine_binaire[i:i+4], 2))[2:] for i in range(0, len(chaine_binaire), 4)]
    return ''.join(hexadecimals).upper()