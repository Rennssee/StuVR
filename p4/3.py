def format_ingredients(items=None):
    if len(items) < 2:
        return "and ".join(items)
    p1 = ", ".join(items[:-1])
    full = p1 + " and " + items[-1]
    return full


print(format_ingredients(items=["2 eggs"]))
