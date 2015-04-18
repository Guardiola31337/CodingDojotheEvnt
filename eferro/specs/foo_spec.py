# -*- coding: utf-8 -*-

from expects import *
from hamcrest import *
from doublex import *

from collections import Counter

PRECIO_UNITARIO = 8
LIBRO1 = 'libro1'
LIBRO2 = 'libro2'
LIBRO3 = 'libro3'

def precioLibros(libros):
    contadores = Counter(libros)
    distintos = len(contadores.keys())
    repetidos = len(libros)-distintos

    if distintos == 2:
        return PRECIO_UNITARIO * 2 * 0.95 + PRECIO_UNITARIO * repetidos
    if distintos == 3:
        return PRECIO_UNITARIO * 3 * 0.90 + PRECIO_UNITARIO * repetidos


    return PRECIO_UNITARIO * len(libros)


with context('Harry Potter Kata'):
    
    with describe('comprando de uno en uno'):
        with it('el primero cuesta PRECIO_UNITARIO'):
            expect(precioLibros([LIBRO1])).to(equal(PRECIO_UNITARIO))
        with it('el segundo cuesta PRECIO_UNITARIO'):
            expect(precioLibros([LIBRO2])).to(equal(PRECIO_UNITARIO))

    with describe('comprando dos'):
        with it('dos copias del mismo cuestan 16'):
            expect(precioLibros([LIBRO1, LIBRO1])).to(equal(2 * PRECIO_UNITARIO))
            expect(precioLibros([LIBRO2, LIBRO2])).to(equal(2 * PRECIO_UNITARIO))

        with it('dos copias distintas tienen un descuento de 5'):
            expect(precioLibros([LIBRO1, LIBRO2])).to(equal(16*0.95))
            expect(precioLibros([LIBRO2, LIBRO1])).to(equal(16*0.95))

    with describe('comprando tres'):
        with it('tres iguales cuestan 24'):
            expect(precioLibros([LIBRO1, LIBRO1, LIBRO1])).to(equal(24))

        with it('de los tres, solo dos distintos'):
            expect(precioLibros([LIBRO1, LIBRO1, LIBRO2])).to(equal(16*0.95 + PRECIO_UNITARIO))

        with it('los tres distintos'):
            expect(precioLibros([LIBRO1, LIBRO2, LIBRO3])).to(equal(PRECIO_UNITARIO * 3*0.90))

    with describe('comprando cuatro'):
        with it('tres iguales cuestan 32'):
            expect(precioLibros([LIBRO1, LIBRO1, LIBRO1, LIBRO1])).to(equal(32))