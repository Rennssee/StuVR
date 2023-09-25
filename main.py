base_rate = 40
price_per_km = 10
total_trip = 0


def calculate_trip_price(distance_km):
    global total_trip
    total_trip += 1
    return (distance_km * price_per_km) + base_rate


print(calculate_trip_price(float(input(">>"))))
print(total_trip)
