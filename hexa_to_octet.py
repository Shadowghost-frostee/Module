__author__ = "<828'121>, <Yao>"


def hexadecimal_en_octet(hexadecimal):
    octets = [hexadecimal[i:i+2] for i in range(0, len(hexadecimal), 2)]
    octets_en_decimal = [int(octet, 16) for octet in octets]
    return octets_en_decimal

