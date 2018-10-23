# encoding: utf-8

class Item(object):
    def __init__(self, description, quantity, amount, additional_data = "", expire = 0):
        self.description = description
        self.quantity = quantity
        self.amount = amount
        self.additional_data = additional_data
        self.expire = expire

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if (value < 0):
            raise ValueError('quantity must be a positive number')
        self.__quantity = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value


class ShoppingCart(object):
    def __init__(self):
        self.__items = []

    def add(self, item: Item):
        new_total = self.total + (item.amount * item.quantity)
        if (new_total < 0):
          raise ValueError('Total amount cannot be less than zero.')
        self.__items.append(item)

    @property
    def items(self):
        return self.__items

    @property
    def total(self):
        return sum(item.amount * item.quantity for item in self.items)

    @property
    def item_quantity(self):
        return sum(item.quantity for item in self.items)
