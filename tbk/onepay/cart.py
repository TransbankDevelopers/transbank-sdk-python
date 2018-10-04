# encoding: utf-8
from __future__ import unicode_literals

class Item(object):
    def __init__(self, description, quantity, amount, additional_data = "", expire = 0):
        self.description = description
        self.quantity = quantity
        self.amount = amount
        self.additional_data = additional_data
        self.expire = expire

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError('description must be a string')
        self.__description = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise ValueError('quantity must be an integer')
        if (value < 0):
            raise ValueError('quantity must be a positive number')
        self.__quantity = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, int):
            raise ValueError('amount must be an integer')
        if (value < 0):
            raise ValueError('amount must be a positive number')
        self.__amount = value

    @property
    def additional_data(self):
        return self.__additional_data

    @additional_data.setter
    def additional_data(self, value):
        if not isinstance(value, str):
            raise ValueError('additional_data must be a string')
        self.__additional_data = value

    @property
    def expire(self):
        return self.__expire

    @expire.setter
    def expire(self, value):
        if not isinstance(value, int):
            raise ValueError('expire must be an integer')
        self.__expire = value

class ShoppingCart(object):
    def __init__(self):
        self.__items = []

    def add(self, item: Item):
        if isinstance(item, Item):
            self.__items.append(item)
        else:
            raise ValueError("item must be an instance of Item")

    @property
    def items(self):
        return self.__items

    @property
    def total(self):
        total = 0
        for item in self.__items:
            total += item.amount * item.quantity
        return total

    @property
    def item_quantity(self):
        quantity = 0
        for item in self.__items:
            quantity += item.quantity

        return quantity
