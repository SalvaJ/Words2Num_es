#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import unittest
import words2num_es as w2n


class TestW2n(unittest.TestCase):

    def setUp(self):
        """
        carga de las listas con los datos para las pruebas
        ejemplo:
            self.lista_correctos_masculinos =
            self.lista_correctos_femeninos =
            ...
        """
        pass

    def tearDown(self):
        """
        limpia las listas con los datos para pruebas
        ejemplo:
            self.lista_correctos_masculinos =
            self.lista_correctos_femeninos =
        """

    def test_correctos_masculinos(self):
        """
        Del 1 al (10^9)-1 en género masculino.
        Dado una lista de [[numero, texto], ...]
            self.assertEqual(numero, w2n.words2num(texto, debug_mode=2))
        """
        pass

    def test_correctos_femeninos(self):
        """
        Del 1 al (10^9)-1 en género femenino
        Dado una lista de [[numero, texto], ...]
            self.assertEqual(numero, w2n.words2num(texto, debug_mode=2))
        """
        pass

    def test_correctos_apocopados(self):
        """
        Del 1 al (10^9)-1 con formas apocopadas (un, veinitiún)
        Dado una lista de [[numero, texto], ...]
            self.assertEqual(numero, w2n.words2num(texto, debug_mode=2))
        """
        pass

    def test_correctos_acentos(self):
        """
        Del 1 al (10^9)-1 con acentos
        Dado una lista de [[numero, texto], ...]
            self.assertEqual(numero, w2n.words2num(texto, debug_mode=2))

        """
        pass

    def test_correctos_mayusculas(self):
        """
        Del 1 al (10^9)-1 en mayùsculas
        Dado una lista de [[numero, texto], ...]
            self.assertEqual(numero, w2n.words2num(texto, debug_mode=2))
        """
        pass

    def test_error_palabras(self):
        """
        Se levantan excepciones en caso de palabras incorrectas.
        ejemplo:
            self.assertRaises(MyException, w2n.words2num("venticinco", debug_mode=2)
        """
        pass

    def test_errores_sintacticos_grupo(self):
        """
        Se levantan excepciones en caso de errores sintácticos en las
        construcciones de los grupos (1..999)
        ejemplo:
            self.assertRaises(MyException, w2n.words2num("treinta y quince", debug_mode=2)
            self.assertRaises(MyException, w2n.words2num("tres y quinientos", debug_mode=2)
        """
        pass

    def test_errores_sintacticos_multiplos(self):
        """
        Se levantan excepciones en caso de errores sintácticos en las
        construcciones de las magnitudes de grupos:
        [multiplo][grupo][multiplo][grupo][multiplo][grupo]...
        El principal error a dectectar es el incorrecto orden de los
        [multiplos]
        """
        pass


if __name__ == "__main__":
    unittest.main()