# customer input pizza size, toppings, miles away
customer_pizza_size = input("What size pizza would you like to order (small or large)?")
customer_toppings = int(input("How many toppings would you like?"))
customer_miles = int(input("How many miles away is the destination?"))

def pizza_size(customer_pizza_size):
	if customer_pizza_size.lower() == "small":
		return 8
	elif customer_pizza_size.lower() == "large":
		return 12
	else:
		return "Invalid pizza size, please enter small or large."
	
def pizza_toppings(customer_toppings):
	if customer_toppings >= 0:
		return customer_toppings
	else:
		return "Invalid number of toppings, please enter the number of pizza toppings you would like."
	
def pizza_miles(customer_miles):
	if 0 < customer_miles <= 5:
		return 2
	elif customer_miles > 5:
		return (customer_miles - 5) + 2
	else:
		return "Invalid miles, please enter the number of miles to the destination."

pizza_total = pizza_size(customer_pizza_size) + pizza_toppings(customer_toppings) + pizza_miles(customer_miles)

print(f"Your order total is ${pizza_total:.2f}")
	
