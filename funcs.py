def add_numbers(x, y):
    sum = x + y
    return sum

class Basket:
    def __init__(self, goods):
        self.goods = goods

    def __sub__(self, other):
        return Basket(self.goods - other.goods)
if __name__ == '__main__':

    my_basket = Basket({'coffee', 'banana', 'bred'})
    to_remove = Basket({'bred'})

    updated_basket = my_basket - to_remove
    print(updated_basket.goods)