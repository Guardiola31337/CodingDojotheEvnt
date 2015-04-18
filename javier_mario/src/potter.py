__author__ = 'mrodriguez'

import os

class ShoppingCart:
    books = []
    PRICE_BOOK = 8
    NUM_BOOKS = 5
    discount_per_num_books = {
        1: 0,
        2: 0.05,
        3: 0.10,
        4: 0.20,
        5: 0.25,
    }

    def __init__(self):
        self.books = [0 for _ in xrange(self.NUM_BOOKS)]

    def add_book(self, id):
        self.books[id] += 1

    def buy(self):
        price_pack = 0
        while sum(self.books) > 0:
            count_disc = 0
            for book_id in xrange(self.NUM_BOOKS):
                if self.books[book_id] > 0:
                    self.books[book_id] -= 1
                    count_disc += 1

            price_pack += count_disc * self.PRICE_BOOK * (1- self.discount_per_num_books[count_disc])

        return price_pack


