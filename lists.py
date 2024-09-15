food = ['apple', 'coconut', 'banana', 'cherry', 'pear', 'orange', 'grapefruit', 'onion', 'melon', 'watermelon']
print(food)
print(food[7])
food[7] = 'garlic'
print(food)
print(food[7])

food.append('pumpkin')
print(food)
food.extend('12345')  # только str
print(food)
food.extend(['12', 12, 12.3, True])
print(food)
food.remove(True)
print(food)
del food[-2:]
print(food)

print('cherry' in food, 'cherry' not in food)

print(food[0:6])
print(food[0:6:2])
