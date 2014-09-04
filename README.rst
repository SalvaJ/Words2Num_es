Words2Num_es
============

This Python library is a Open Source (BSD License) implementation of an algorithm to parse and convert textual numbers
written in Spanish into its representation of integer number.

Esta librería para Python es una implementación en Código Abierto (Licencia BSD) de un algoritmo para analizar y
convertir numeros cardinales en texto en Español a su representación en cifras de número entero.


STATUS:
=======
- Se encuentra en pleno desarrollo.
- Debido a alguno de sus errores conocidos, ni siquiera está en condiciones de llamarse versión *alfa*.
- Ahora mismo produce salidas de valores intermedios por la *stdout* produciondos con ``print()`` a efectos de depuración.


REQUISITOS:
===========
- Python 3.x
    para su implementación en Python 2.x bastaría con no utilizar ``nonlocal``, cambiándolo por ``global``
- No requiere de ningún otro módulo, ni siquiera de la biblioteca estándar de Python.

CARACTERÍSTICAS:
================
- Converte los números cardinales en español de texto (numerales cardinales) a cifra arábiga (0..9).
- Sigue las normas de la **Real Academia Española (R.A.E.)** `Diccionario Panhispánico de Dudas: <http://lema.rae.es/dpd/srv/search?id=rqV8h362gD62vc21qB>`_
- Soporta tanto palabras en mayúsculas como minúsculas o capitalizadas (incluso mezcladas).
	- *VEINTITRÉS*
	- *veintitrés*
	- *Veintitrés*
	- *VEINTITRéS*
- Soporta las palabras con vocales acentuadas y también las admite sin acento.
	- *veintitrés*
	- *veintitres*
- Genera Excepción por palabras desconocidas o mal escritas conforme a la R.A.E.
	- *ventitres*
	- *venticinco*
- Genera Excepción por errores sintácticos. (incompleto)
	- *veinte y tres*
	- *tres cientos*
- Utiliza la llamada  `Escala Larga de Numeración: <http://es.wikipedia.org/wiki/Escalas_num%C3%A9ricas_larga_y_corta>`_ (incompleto).
- No soporta construcciones mixtas de texto y cifras usadas muy usadas en prensa latinoamericana.
	- 30 mil

ERRORES CONOCIDOS:
==================
- La ausencia de un grupo significativo no multiplicador delante del *"mil"* omite su cómputo.
	- *mil novecientos setenta -> 970*
	- *un millón mil -> 1000000*
- Las magnitudes a partir de *"mil millones"* no funcionan.


Ejemplo:
========

.. code-block:: pycon

    >>> import Words2Num_es as w2n
    >>> w2n.words2num("Un Millón trescientos ochenta y Siete Mil Ochocientos VEINTITRÉS")
    ['veintitrés', 'ochocientos', 'mil', 'siete', 'y', 'ochenta', 'trescientos', 'millón', 'un']
    veintitrés
    ochocientos
    mil
    siete
    y
    ochenta
    trescientos
    millón
    un
    {0: 823, 1: 387, 2: 1}
    1387823
    >>>
