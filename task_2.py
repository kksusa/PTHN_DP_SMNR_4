def take_kwargs(**kwargs):
    dictionary = {}
    for key, value in kwargs.items():
        try:
            hash(value)
        except:
            value = str(value)
        dictionary[value] = key
    return dictionary


print(take_kwargs(math=5, physics=[4], literature=3))
