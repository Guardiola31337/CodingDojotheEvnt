# -*- coding: utf-8 -*-

from expects import *
from hamcrest import *
from doublex import *

from collections import Counter

UNIT_PRICE = 8
BOOK1 = 'book1'
BOOK2 = 'book2'
BOOK3 = 'book3'

def books_price(books):
    discounts = {
        2: 0.95,
        3: 0.90,
    }
    book_counter = Counter(books)
    differents = len(book_counter.keys())
    repeated = len(books)-differents

    return differents * discounts.get(differents, 1) * UNIT_PRICE + repeated * UNIT_PRICE

with context('Harry Potter Kata'):
    
    with describe('buying one by one'):
        with it('the cost of the first is UNIT_PRICE'):
            expect(books_price([BOOK1])).to(equal(UNIT_PRICE))
        with it('the cost of the second is UNIT_PRICE'):
            expect(books_price([BOOK2])).to(equal(UNIT_PRICE))

    with describe('buying two'):
        with it('the cost of two copys of the same book is twice the unit price'):
            expect(books_price([BOOK1, BOOK1])).to(equal(16))
            expect(books_price([BOOK2, BOOK2])).to(equal(16))

        with it('the cost of two different books has a 5percent discount'):
            expect(books_price([BOOK1, BOOK2])).to(equal(16*0.95))
            expect(books_price([BOOK2, BOOK1])).to(equal(16*0.95))

    with describe('buying three books'):
        with it('the cost of three copies is 24'):
            expect(books_price([BOOK1, BOOK1, BOOK1])).to(equal(24))

        with describe('when two book are different'):
            with it('the cost is 23.5 (two books with 5percent discount)'):
                expect(books_price([BOOK1, BOOK1, BOOK2])).to(equal(16*0.95 + UNIT_PRICE))
        with describe('when all are differents'):
            with it('the cost is 21.6 (three books with 10percent discount)'):
                expect(books_price([BOOK1, BOOK2, BOOK3])).to(equal(UNIT_PRICE * 3*0.90))

    with describe('buing four books'):
        with it('the cost of four copies is 32'):
            expect(books_price([BOOK1, BOOK1, BOOK1, BOOK1])).to(equal(32))