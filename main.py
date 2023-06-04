from funcs import add_numbers, Basket

num_1 = 15
num_2 = 20

print(add_numbers(num_1, num_2))


my_basket = Basket({'coffee', 'banana', 'bred'})
to_remove = Basket({'bred'})

updated_basket = my_basket - to_remove
print(updated_basket.goods)
