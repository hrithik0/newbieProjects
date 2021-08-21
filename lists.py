list_num = [4, 5, 6, 3, 10]
max_num = 0
for i in range(len(list_num) - 1):
    if list_num[i] > list_num[i + 1]:
        max_num = list_num[i]
    else:
        max_num = list_num[i + 1]
print(max_num)

