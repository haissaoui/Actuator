# This function convert the interest rate into discount rate
def interest_to_discount_converter(i):
    d = 1 - 1 / (1+i)
    return d
i = 0.06
print(interest_to_discount_converter(i))
