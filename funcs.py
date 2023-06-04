def add_numbers(x, y):
    sum = x + y
    return sum

class Basket:
    def __init__(self, goods):
        self.goods = goods

    def __sub__(self, other):
        return Basket(self.goods - other.goods)


