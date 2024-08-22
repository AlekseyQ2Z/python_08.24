quantity = int(input("Введите количество арбузов: "))
min = 3001
max = -1
if quantity > 0:
    for i in range(quantity):
        weight = int(input("Введите вес арубза: "))
        if weight < min:
            min = weight
        elif weight > max:
            max = weight
else:
    print("Арбузы отсутсвуют")
print(f"Максимальный вес арбуза {max}, минимальный вес арбуза {min}")