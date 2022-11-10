import bc_versiasli
from bc_versiasli import create_spend_chart

food = bc_versiasli.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
#food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())
#clothing = bc_versiasli.Category("Clothing")
#food.transfer(50, clothing)
#clothing.withdraw(25.55)
#clothing.withdraw(100)
#auto = bc_versiasli.Category("Auto")
#auto.deposit(1000, "initial deposit")
#auto.withdraw(15)


print(food)
#print(clothing)
#print(auto)

#print(create_spend_chart([food, clothing, auto]))