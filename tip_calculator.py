# Tip calculator using ternary operator

# Initial logic for calculating tip using ternary operator

# Example bill amount
bill_amount = 275

# Determine the tip amount
tip = bill_amount * 0.15 if 50 <= bill_amount <= 300 else bill_amount * 0.20

# Output the result (for verification)
print(f"The bill amount is ${bill_amount}, and the calculated tip is ${tip:.2f}")

# Tip calculator with calcTip function

# Function to calculate the tip based on the bill amount
def calcTip(bill):
    return bill * (0.15 if 50 <= bill <= 300 else 0.20)

# Testing the calcTip function
test_bill = 100
test_tip = calcTip(test_bill)
print(f"For a bill of ${test_bill}, the tip is ${test_tip:.2f}")
