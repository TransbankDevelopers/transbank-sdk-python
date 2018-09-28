import unittest

from onepay.cart import ShoppingCart, Item

class CartTestCase(unittest.TestCase):
    def test_create_single_item(self):
        item = Item("Ropa", 1, 1000)
        self.assertIsNotNone(item)
        self.assertEqual(item.description, "Ropa")
        self.assertEqual(item.quantity, 1)
        self.assertEqual(item.expire, 0)
        self.assertEqual(item.additional_data, "")

    def test_shopping_cart_add_items(self):
        cart = ShoppingCart()
        cart.add(Item("Ropa", 1, 1000))
        cart.add(Item("Envio", 1, 500))

        self.assertEqual(len(cart.get_items()), 2)

    def test_calculate_cart_total(self):
        cart = ShoppingCart()

        self.assertEqual(cart.get_total(), 0)

        cart.add(Item("Ropa", 1, 1000))
        self.assertEqual(cart.get_total(), 1000)

        cart.add(Item("Envio", 1, 500))
        self.assertEqual(cart.get_total(), 1500)

    def test_validations(self):
        with self.assertRaises(ValueError):
            Item(0, 0, 0)
        with self.assertRaises(ValueError):
            Item("", "", 0)
        with self.assertRaises(ValueError):
            Item("", 0, "")
        with self.assertRaises(ValueError):
            Item("", 0, 0, 0)
        with self.assertRaises(ValueError):
            Item("", 0, 0, "","")
