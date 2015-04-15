"""This file should have our melon-type classes in it."""

class Melon(object):
    def get_base_price(self):
        return 5.0

    def get_total_price(self, qty = 1):
        total = qty * (self.get_base_price() + self.increase_on_base_price)
        if self.imported:
            total = total * 1.5
        if self.shape == "square":
            total = total * 2
        return total

class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    increase_on_base_price = 0

    def get_price(self, qty=1):
        """Calculate price, given a number of melons ordered."""
        total = super(WatermelonOrder, self).get_total_price(qty)
        if qty >=3:
            total = total * 0.75
        return total


class CantaloupeOrder(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]
    increase_on_base_price = 0

    def get_price(self, qty=1):
        total = super(CantaloupeOrder, self).get_total_price(qty)
        if qty >= 5:
            total = total * 0.5
        return total

class CasabaOrder(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Summer", "Fall", "Winter", "Spring"]
    increase_on_base_price = 1.0

    def get_price(self, qty = 1):
        return super(CasabaOrder, self).get_total_price(qty)

class SharlynOrder(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    increase_on_base_price = 0

    def get_price(self, qty=1):
        return super(SharlynOrder, self).get_total_price(qty)

class SantaClausOrder(Melon):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]
    increase_on_base_price = 0

    def get_price(self, qty=1):
        return super(SantaClausOrder, self).get_total_price(qty)

class ChristmasOrder(Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter", "Spring"]
    increase_on_base_price = 0

    def get_price(self, qty=1):
        return super(ChristmasOrder, self).get_total_price(qty)

class HornedMelonOrder(Melon):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    increase_on_base_price = 0

    def get_price(self, qty=1):
        return super(HornedMelonOrder, self).get_total_price(qty)

class XiguaOrder(Melon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]
    increase_on_base_price = 0

    def get_price(self, qty=1):
        return super(XiguaOrder, self).get_total_price(qty)

class OgenOrder(Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]
    increase_on_base_price = 1.0

    def get_price(self, qty=1):
        return super(OgenOrder, self).get_total_price(qty)