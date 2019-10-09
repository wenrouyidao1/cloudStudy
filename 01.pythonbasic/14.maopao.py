list01 = [2, 4, 1, 10, 99, 88]
for value in range(len(list01)):
    for j in range(len(list01) -value -1):
        if list01[j] > list01[j+1]:
            list01[j], list01[j+1] = list01[j+1], list01[j]

print(list01)