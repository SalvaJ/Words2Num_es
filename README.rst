Words2Num_es
============

This Python library is a Open Source (BSD License) implementation of a function to parse and convert textual numbers
written in Spanish into its representation of integer number.


Esta librería para Python es una implementación en Código Abierto (Licencia BSD) de una función para analizar y 
convertir numeros cardinales en texto en Español a su representación en cifras de número entero.



Example:
========

.. code-block:: pycon

    >>> import Words2Num_es as w2n
    >>> w2n.words2num("Un Millón trescientos ochenta y Siete Mil Ochocientos VEIN
    TITRÉS")
    ['veintitrés', 'ochocientos', 'mil', 'siete', 'y', 'ochenta', 'trescientos', 'mi
    llón', 'un']
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
