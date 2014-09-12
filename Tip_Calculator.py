"""The first exercise of the class
the goal is to input the amount of the bill, add sales tax and tip,
and print to screen what's the total amount that you should pay"""

#define a function to do the calculation 
def tip_calculator(bill):
    tax = 0.0625
    tip = 0.15
    bill = float(bill)*(1+0.0625+0.15)
    return bill

#take in the original price of the meal
x = input("Hellp, I am your tip calculator. Please input your bill:")
#print the total price of the meal to the screen
print ("You should pay: %5.3f" %tip_calculator(x))

