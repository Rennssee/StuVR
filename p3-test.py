def cost_delivery(quantity, *_, discount=0):
    summ1 = 5 + (quantity - 1) * 2
    cost = summ1 * (1 - discount)
    return cost


print(cost_delivery(5, 5, 5, 33, discount=0.5))
