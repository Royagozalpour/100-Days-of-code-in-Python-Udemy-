import random
names_string = input("Enter names separated by comma and space: ")
names = names_string.split(", ")
random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")
