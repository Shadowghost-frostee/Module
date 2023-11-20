__author__ = "<828'121>, <Yao>"

def dezimal_zu_hexadezimal(zahl):
    if zahl == 0:
        return "0"
    hexadezimalzahl = ""
    hexadezimalzeichen = "0123456789ABCDEF"
    while zahl > 0:
        rest = zahl % 16
        hexadezimalzahl = hexadezimalzeichen[rest] + hexadezimalzahl
        zahl = zahl // 16
    return hexadezimalzahl

print(dezimal_zu_hexadezimal(0.12))
