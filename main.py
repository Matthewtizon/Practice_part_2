# Create an app that can check how many pizzas did a person orders and its percentage and the price of the pizza

# declare a 3-variable user name
name_1 = input("What is your name: ")
name_2 = input("What is your name: ")
name_3 = input("What is your name: ")

slices_in_the_pizza = input("How many slices in the pizza: ")
price_of_the_pizza = input("What is the price of the pizza: ")

percentage_ate_by_person_1 = input(name_1 + " what percentage of the pizza you have ate: ")
percentage_ate_by_person_2 = input(name_2 + " what percentage of the pizza you have ate: ")
percentage_ate_by_person_3 = input(name_3 + " what percentage of the pizza you have ate: ")

number_of_slices_ate_person_1 = float(percentage_ate_by_person_1) * float(slices_in_the_pizza)
number_of_slices_ate_person_2 = float(percentage_ate_by_person_2) * float(slices_in_the_pizza)
number_of_slices_ate_person_3 = float(percentage_ate_by_person_3) * float(slices_in_the_pizza)

price_payed_by_name_1 = float(percentage_ate_by_person_1) * float(price_of_the_pizza)
price_payed_by_name_2 = float(percentage_ate_by_person_2) * float(price_of_the_pizza)
price_payed_by_name_3 = float(percentage_ate_by_person_3) * float(price_of_the_pizza)

print(name_1 + " ordered " + str(slices_in_the_pizza) + " slices of pizza" + " and payed " + str(price_payed_by_name_1)
      + " dollars")
print(name_2 + " ordered " + str(slices_in_the_pizza) + " slices of pizza" + " and payed " + str(price_payed_by_name_2)
      + " dollars")
print(name_3 + " ordered " + str(slices_in_the_pizza) + " slices of pizza" + " and payed " + str(price_payed_by_name_3)
      + " dollars")








