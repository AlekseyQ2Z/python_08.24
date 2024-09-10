#def transformation(temp):
#    return temp

transformation = lambda x: x

values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print("Ok")
else:
    print("fail")