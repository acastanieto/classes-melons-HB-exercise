"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    base_price = 5.0 

    def get_price(self, qty=1):
        """Calculate price, given a number of melons ordered."""
        # base cost $5 each
        # if you buy 3 or more -> all are 75% off of total
        total = qty * self.base_price
        if qty >=3:
            total = total * 0.75
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]
    base_price = 5.0

    def get_price(self, qty=1):
        total = qty * self.base_price
        if qty >= 5:
            total = total * 0.5
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Summer", "Fall", "Winter", "Spring"]
    base_price = 6.0

    def get_price(self, qty = 1):
        total = qty * self.base_price
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total

class Sharlyn(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    base_price = 5.0

    def get_price(self, qty=1):
        total = qty * self.base_price
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]
    base_price = 5.0

    def get_price(self, qty = 1):
        total = qty * self.base_price
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter", "Spring"]
    base_price = 5.0

    def get_price(self, qty=1):
        total = qty * self.base_price
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    base_price = 5.0

    def get_price(self, qty = 1):
        total = qty * self.base_price
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]
    base_price = 5.0

    def get_price(self, qty=1):
        total = qty * self.base_price
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]
    base_price = 6.0

    def get_price(self, qty=1):
        total = qty * self.base_price
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total