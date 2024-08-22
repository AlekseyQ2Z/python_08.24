number = int(input("Введите число и я напишу все целые степени двойки, не превосходящие этого числа: "))
degree = 1
print(f"Вот все целые степени двойки, не превосходящие число {number}. \n{degree}")
while degree < number:
    degree *= 2
    if degree < number:
        print(degree)