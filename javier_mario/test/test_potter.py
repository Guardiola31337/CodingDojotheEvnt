import unittest

from potter import ShoppingCart


class TestPotter(unittest.TestCase):

    shopping_cart = None

    def setUp(self):
      self.shopping_cart = ShoppingCart()

    def test_buy_one_book(self):
        self.shopping_cart.add_book(id = 1)
        value = self.shopping_cart.buy()
        self.assertEqual(value, 8, 'Should be 8 and it gives %f' % value)

    def test_buy_two_books_different(self):
        self.shopping_cart.add_book(id = 1)
        self.shopping_cart.add_book(id = 2)
        value = self.shopping_cart.buy()
        self.assertEqual(value, 15.2, 'Should be 15,20 and it is %f' % value)

    def test_buy_two_books_equals(self):
        self.shopping_cart.add_book(id = 1)
        self.shopping_cart.add_book(id = 1)
        value = self.shopping_cart.buy()
        self.assertEqual(value, 16, 'Should be 16 and it is %f' % value)

    def test_buy_whole_collection(self):
        self.shopping_cart.add_book(id = 0)
        self.shopping_cart.add_book(id = 1)
        self.shopping_cart.add_book(id = 2)
        self.shopping_cart.add_book(id = 3)
        self.shopping_cart.add_book(id = 4)
        value = self.shopping_cart.buy()
        self.assertEqual(value, 30)

    def test_five_books_group_by_three_and_two(self):
        self.shopping_cart.add_book(id = 0)
        self.shopping_cart.add_book(id = 1)
        self.shopping_cart.add_book(id = 2)
        self.shopping_cart.add_book(id = 0)
        self.shopping_cart.add_book(id = 1)
        value = self.shopping_cart.buy()
        self.assertEqual(value, 36.8)

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPotter)
    unittest.TextTestRunner(verbosity=2).run(suite)
