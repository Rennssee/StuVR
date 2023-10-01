def lookup_key(data, value):
    keys = []

    for i, f in data.items():
        if f == value:
            keys.append(i)

    return keys


my_dict = {"key1": "value1", "key2": "value2", "key3": "value1", "key4": "value3"}

print(lookup_key(my_dict, "value1"))
