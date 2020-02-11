from People_class import People, Customers
from food_items_class import FoodItem, Combos
from Orders_Class import Order
# as a restaurant owner I can create new customers

customer1 = Customers('John', '21 down town abbey, London')
customer2 = Customers('Olly', '80 avenue, London')


#As a restaurant owner, I can create new food items

# 3 mains
main1 = FoodItem('Sea Bass', 17.5, ['sea bass fish'])
main2 = FoodItem('omelate du Formage Avec Champignon',9, ['Eggs', 'cheese', 'mushrooms'])
main3 = FoodItem('Fiorentina', 5.50, ['Tomato sauce', 'spinach', 'eggs'])

# 3 sides
side1 = FoodItem('Garlic bread', 4, ['bread', 'garlic'])
side2 = FoodItem('cheesy garlicy bread', 5, ['bread', 'garlic', 'cheese'])

# 3 drinks
drink1 = FoodItem('water', 3, ['water'])
drink2 = FoodItem('Coke', 3, ['others'])
drink3 = FoodItem('Smoothies', 4 , ['oranges', 'carrots', 'kiwi'])

#3 combos

#As a restaurant owner I can create new orders and add food items for a customer.
#opening a tab to order
order1 = Order(customer1)
order1.add_items_order(main3)
order1.add_items_order(drink3)

