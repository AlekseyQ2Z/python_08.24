bush = list(map(int, input("Введите количество ягод через пробел на кустах: ")
                .split()))
bush.extend([bush[0], bush[1]])
max_sum = 0
for i in range(len(bush)-2):
    sum = bush[i] + bush[i+1] + bush[i+2]
    if sum > max_sum:
        max_sum = sum
print(max_sum)