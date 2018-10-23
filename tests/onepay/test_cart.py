import unittest

from transbank.onepay.cart import ShoppingCart, Item

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

        self.assertEqual(len(cart.items), 2)

    def test_calculate_cart_total(self):
        cart = ShoppingCart()

        self.assertEqual(cart.total, 0)

        cart.add(Item("Ropa", 1, 1000))
        self.assertEqual(cart.total, 1000)

        cart.add(Item("Envio", 1, 500))
        self.assertEqual(cart.total, 1500)

    def test_can_add_items_to_cart_with_item_negative_value(self):
        cart = ShoppingCart()

        self.assertEqual(cart.total, 0)

        cart.add(Item("Ropa", 1, 200))
        self.assertEqual(cart.total, 200)

        cart.add(Item("Descuento", 1, -10))
        self.assertEqual(cart.total, 190)

    def test_can_add_items_to_cart_with_item_negative_value_greater_than_total_amount(self):
        cart = ShoppingCart()

        self.assertEqual(cart.total, 0)

        cart.add(Item("Ropa", 1, 200))
        self.assertEqual(cart.total, 200)

        with self.assertRaisesRegex(ValueError, "Total amount cannot be less than zero."):
            cart.add(Item("Descuento", 1, -201))

    def test_calculate_cart_quantity(self):
        cart = ShoppingCart()

        self.assertEqual(cart.item_quantity, 0)

        cart.add(Item("Ropa", 2, 1000))
        self.assertEqual(cart.item_quantity, 2)

        cart.add(Item("Envio", 3, 500))
        self.assertEqual(cart.item_quantity, 5)

    def test_positive_item_validations(self):
        with self.assertRaisesRegex(ValueError, "quantity must be a positive number"):
            Item("", -1, 0)
