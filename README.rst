Words2Num_es
============

This Python library is a Open Source (BSD License) implementation of an algorithm to parse and convert textual numbers
written in Spanish language into its representation of integer number.

Esta librería para Python es una implementación en Código Abierto (Licencia BSD) de un algoritmo para analizar y
convertir numeros cardinales en texto en Español a su representación en cifras de número entero.


EJEMPLO:
========

.. code-block:: pycon

    >>> import Words2Num_es as w2n
    >>> w2n.words2num("Un Millón trescientos ochenta y Siete Mil Ochocientos VEINTITRÉS")
    1387823
    >>>


STATUS:
=======
- Se encuentra en pleno desarrollo.
- Debido a alguno de sus errores conocidos, ni siquiera está en condiciones de llamarse versión *alfa*.

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

ALGORITMO:
==========
Existen bastantes algoritmos para convertir números a (texto) letras en idioma Español, en los lenguajes de programación
más usados.  Yo mismo escribí uno hace algunos años en Visual Basic que convertía importes en euros a palabras para su
uso como macro en Word.

Ahora necesitaba justo lo contrario.  Después de mucho buscar tanto en Github, como en Sourceforge y en Google en
general, no he encontrado ningún algoritmo en ningún lenguaje de programación que realice la conversión de texto a
número en idioma Español.  No sé si es que dicho algoritmo es de poca utilidad (no lo creo, su uso en *data mining*,
análisis lexicográficos de dominios y redes sociales,...) o su difícil implementación en el idioma Español (con
numerosas irregularidades) han provocado la inexistencia de algoritmo alguno en código abierto.  No me cabe duda de que
existen soluciones propietarias en programas de OCR, *speech-to-text*, *data mining*, pero el problema es que no hay
**ninguno Open Source**.

Después de repasar el código de algún algoritmo para idioma Inglés tuve que descartar su implementación al idioma
Español y decidí partir de cero.

Por ello creo que éste podría ser el **primer algoritmo Open Source para idioma Español que convierte números en letra a
su equivalente en cifras numéricas**.


CONTRIBUCIONES:
===============
Cualquier ayuda, contribución y/o colaboración será bienvenida.  Contactar con: salvajgb@gmail.com o por medio de un
*issue* en Github.