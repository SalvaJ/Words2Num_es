#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This library is a implementation of an algorithm to parse and convert
# textual numbers written in Spanish into their integer representations.
#
# This code is open source according to the BSD (2 clause) License.
#
# Copyright (c) 2014 Salva Jimenez.


unidades = {
    "un": 1, "uno": 1, "una": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
}

decenas_atomicos = {
    "diez": 10,
    "once": 11,
    "doce": 12,
    "trece": 13,
    "catorce": 14,
    "quince": 15,
    "dieciséis": 16, "dieciseis": 16,
    "diecisiete": 17,
    "dieciocho": 18,
    "diecinueve": 19,
    "veinte": 20,
    "veintiún": 21, "veintiun": 21, "veintiuno": 21, "veintiuna": 21,
    "veintidós": 22, "veintidos": 22,
    "veintitrés": 23, "veintitres": 23,
    "veinticuatro": 24,
    "veinticinco": 25,
    "veintiséis": 26, "veintiseis": 26,
    "veintisiete": 27,
    "veintiocho": 28,
    "veintinueve": 29,
}

decenas = {
    "treinta": 30,
    "cuarenta": 40,
    "cincuenta": 50,
    "sesenta": 60,
    "setenta": 70,
    "ochenta": 80,
    "noventa": 90,
}

centenas = {
    "cien": 100, "ciento": 100,
    "doscientos": 200, "doscientas": 200,
    "trescientos": 300, "trescientas": 300,
    "cuatrocientos": 400, "cuatrocientas": 400,
    "quinientos": 500, "quinientas": 500,
    "seiscientos": 600, "seiscientas": 600,
    "setecientos": 700, "setecientas": 700,
    "ochocientos": 800, "ochocientas": 800,
    "novecientos": 900, "novecientas": 900
}

multiplos = {
    "mil": 1,
    "millón": 2, "millon": 2, "millones": 2,
    "billón": 3, "billon": 3, "billones": 3
}

multiplicadores = {
    0: 10 ** 0,
    1: 10 ** 3,
    2: 10 ** 6,
    3: 10 ** 12
}

conjuncion = {"y": 1}   # TODO handle "y" between "decenas" and "unidades"


class MyExcepcion(Exception):
    """
    .. py:class:: MyExcepcion(Exception)
        To raise exceptions when sintax error are found in string_to_convert
    """
    def __init__(self, msg):
        """
        .. py:method:: __init__(self, msg)
            Extend `Exception.__init__()` method
        :param str msg: (required), the message of the error to display
        :return none:
        """
        Exception.__init__(self, msg)


def words2num(string_to_convert, debug_mode=0):
    """
    .. py:function:: words2num(string_to_convert, debug_mode=0)
        Main function to parse the text numbers.
    :param str string_to_convert: (required) the phrase to parse.
    :param int debug_mode: (optional) 0= no debug, 1= stdout, 2= log file
    :return cifra_numero: the value of the whole phrase.
    :rtype int:
    :raise MyException: if syntax error or unknown word is found.
    """

    if debug_mode == 2:
        import logging

        FORMAT = '%(levelname)s %(message)s'
        logging.basicConfig(filename='w2n_debug.log', level=logging.DEBUG, format=FORMAT)

    def debug(func):
        def _debug(msg):
            if debug_mode == 1:
                print(msg)
                func(msg)   # For future uses
            if debug_mode == 2:
                logging.debug(msg)
                func(msg)   # For future uses
        return _debug

    @debug
    def echo(msg):
        pass

    def grupo(p):
        """
        .. py:function:: grupo(p)
            local function to parse words until hundreds are completed
        :param str p: the word to evaluate
        :return cifra_grupo: the value in units of the group
        :rtype int:
        :raise MyException: if syntax error or unknown word is found.
        """
        echo(p)    # debug purpose
        nonlocal sw_grupo, cifra_grupo, cifra_total, indice_multiplos
        if p in multiplos:
            cifra_total[indice_multiplos] = cifra_grupo
            indice_multiplos = multiplos[p]
            cifra_grupo = 0
            sw_grupo = 0b0000
        elif p in unidades:
            if sw_grupo == 0:
                cifra_grupo = unidades[p]
                sw_grupo += 0b0001
            else:
                raise MyExcepcion("Error en -%s-, Sintáxis Incorrecta!" % p)
        elif p in decenas_atomicos:
            if sw_grupo == 0:
                cifra_grupo = decenas_atomicos[p]
                sw_grupo += 0b0010
            else:
                raise MyExcepcion("Error en -%s-, Sintáxis Incorrecta!" % p)
        elif p in decenas:
            if sw_grupo < 0b0010:
                cifra_grupo += decenas[p]
                sw_grupo += 0b0100
            else:
                raise MyExcepcion("Error en -%s-, Sintáxis Incorrecta!" % p)
        elif p in centenas:
            if sw_grupo < 0b1000:
                cifra_grupo += centenas[p]
                sw_grupo += 0b1000
            else:
                raise MyExcepcion("Error en -%s-, Sintáxis Incorrecta!" % p)
        else:
            if p in conjuncion:
                pass    # TODO handle "y" between "decenas" and "unidades"
            else:
                raise MyExcepcion("Error en -%s-, Palabra Desconocida!" % p)
        return cifra_grupo

    lista_cifra_texto = string_to_convert.lower().split()
    lista_cifra_texto.reverse()
    echo(lista_cifra_texto)    # debug purpose

    cifra_numero = 0
    cifra_total = {}
    indice_multiplos = 0
    sw_multiplos = 0b0000   # TODO control the flow of thousands+
    cifra_grupo = 0
    sw_grupo = 0b0000
    for palabra in lista_cifra_texto:
        grupo(palabra)
    cifra_total[indice_multiplos] = cifra_grupo
    echo(cifra_total)  # debug purpose
    for i, j in cifra_total.items():
        cifra_numero += j * multiplicadores[i]
    return cifra_numero

if __name__ == "__main__":
    from sys import version_info
    # Checking python version to use the correct input function
    if version_info[0] == 3:
        entrada = input
    else:
        entrada = raw_input

    cifra_texto = entrada("Introduzca la cantidad en texto: ")
    print(words2num(cifra_texto, debug_mode=1))
