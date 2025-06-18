# 1. Define the Problem:
'''
Create a Python script named pizza_order_cost.py that calculates the total cost of a pizza order based on Pizza size, Number of toppings, Delivery distance.
'''

# 2. Design a Solution
'''
1. Start
2. Prompt the user for inputs for pizza size, number of toppings, and delivery distance in miles.

3. Calculate the base cost of the pizza using conditional statements
	if pizza size input = small
		return 8
	else if pizza size input = large
		return 12
	else 
		Invalid pizza size, please enter small or large

4. Calculate the cost of toppings
	if number of toppings input is >= 0
		return number of toppings input
	else 
		Invalid number of toppings, please enter the number of pizza toppings you would like

5. Calculate the delivery fee
	if 0 < delivery distance input <= 5 
		return 2
	else if 5 < delivery distance input <= 20 
		return (delivery distance input - 5) + 2
	else
		Invalid miles, please enter the number of miles to the destination (up to 20 miles)

6. Sum up the total cost by adding up size, toppings, delivery fee

7. Display the result using an f-string

8. End

Challenge: What if Delivery Distance is 100 miles away?
Will return, Invalid miles, please enter the number of miles to the destination (up to 20 miles).

'''
# 3. Implement the Solution

# customer input pizza size, toppings, miles away
customer_pizza_size = input("What size pizza would you like to order (small or large)?")
customer_num_toppings = int(input("How many toppings would you like?"))
customer_delivery_miles = int(input("How many miles away is the destination (up to 20 miles)?"))

# pizza size pricing
def pizza_size(customer_pizza_size):
	if customer_pizza_size.lower() == "small":
		return 8
	elif customer_pizza_size.lower() == "large":
		return 12
	else:
		return "Invalid pizza size, please enter small or large."

# pizza topping pricing 	
def num_pizza_toppings(customer_num_toppings):
	if customer_num_toppings >= 0:
		return customer_num_toppings
	else:
		return "Invalid number of toppings, please enter the number of pizza toppings you would like."

# Pizza miles pricing	
def delivery_miles(customer_delivery_miles):
	if 0 < customer_delivery_miles <= 5:
		return 2
	elif 5 < customer_delivery_miles <=20 :
		return (customer_delivery_miles - 5) + 2
	else:
		return "Invalid miles, please enter the number of miles to the destination (up to 20 miles)."

# Calculate pizza total
pizza_total = pizza_size(customer_pizza_size) + num_pizza_toppings(customer_num_toppings) + delivery_miles(customer_delivery_miles)

# Print pizza total to customer
print(f"Your order total is ${pizza_total:.2f}")
	
