def amount_payment(payment=[]):
    add_amount = [x for x in payment if x > 0]
    sum = 0
    for value in add_amount:
        sum = sum + value
    return sum


print(amount_payment([1, -3, 4]))
