# encoding: utf-8
from __future__ import unicode_literals

class Item(object):
    def __init__(self, description, quantity, amount, additional_data = "", expire = 0):
        if not isinstance(description, str):
            raise ValueError('description must be a string')
        if not isinstance(quantity, int):
            raise ValueError('quantity must be an integer')
        if not isinstance(amount, int):
            raise ValueError('amount must be an integer')
        if not isinstance(additional_data, str):
            raise ValueError('additional_data must be a string')
        if not isinstance(expire, int):
            raise ValueError('expire must be an integer')

        if (quantity < 0):
            raise ValueError('quantity must be a positive number')
        if (amount < 0):
            raise ValueError('amount must be a positive number')

        self.description = description
        self.quantity = quantity
        self.amount = amount
        self.additional_data = additional_data
        self.expire = expire

class ShoppingCart(object):
    def __init__(self):
        self.__items = []
        self.__total = 0
    def add(self, item):
        self.__items.append(item)
        self.__total += item.amount * item.quantity

    def get_items(self):
        return self.__items

    def get_total(self):
        return self.__total
