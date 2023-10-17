##This program was created by Merdan Garlyyev. I am taking CS230-002-10521 class this semester.
## The name of my program is "TheHungryKnight.py". Deadline for this is Sept 19,2022 until 11:59 pm
## I built my program in the way that it greets the Knight. It offers him and his men several different foods and drink. According to what the guests want, the program calculates the price and gives the total value including taxes.

print("Welcome to the finest Inn and Tavern in Jacksonville, AL")
print("Hello the owner of tavern. I am a Knight of this town. My men and I are very hungry and would like to eat in your place")
print("It's very nice to see you and your men, Sir Knight. It's my pleasure to assist you today in my tavern")

name_of_knight = input("What's your name dear Sir, Knight? \n")
## In order to give response for output in new line just add "\n" after the end of last word of string then close quote
## The name of knight is Kevin

characteristic = input("What's your main characteristic? \n")
## His main characteristic is being Strong

address_to_knight = ("Sir " + name_of_knight + " the " + characteristic)
print("Nice to meet you " + address_to_knight)
print("These are foods and drink that are available in my tavern: ")
food_item1 = ("fried chicken")
food_item2 = ("pizza")
food_item3 = ("lasagna")
food_item4 = ("nuggets")
drink = ("tequila")
print(food_item1 + ", " + food_item2 + ", " + food_item3 + ", " + food_item4 + ", and " + drink + ".")
food_cost1 = 15.10
food_cost2 = 3.49
food_cost3 = 5.17
food_cost4 = 1.19
drink_cost = 2.15
amount1 = input("How many of " + food_item1 + " will your party require us to prepare, " + address_to_knight + "? \n")
## 2 items
amount2 = input("How many of " + food_item2 + " will your party require us to prepare, " + address_to_knight + "? \n")
## 5 items
amount3 = input("How many of " + food_item3 + " will your party require us to prepare, " + address_to_knight + "? \n")
## 4 items
amount4 = input("How many of " + food_item4 + " will your party require us to prepare, " + address_to_knight + "? \n")
## 12 items
amount5 = input("How many of " + drink + " will your party require us to prepare, " + address_to_knight + "? \n")
## 10 items

subtotal = (float(food_cost1) * float(amount1) + float(food_cost2) * float(amount2) + float(food_cost3) * float(amount3) + float(food_cost4) * float(amount4) + float(drink_cost) * float(amount5))
print("Subtotal price = " + str(subtotal) + " silver pieces")
taxes = (subtotal * 1.05)
print("The total cost with taxes = " + str(taxes) + " silver pieces")
print("Thank you for coming and have a great rest of your day!")

