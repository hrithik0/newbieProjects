numbers = [5,3,4,6,7,5,8,9,7]
numbers.pop()
numbers.sort(reverse=True)
# print(numbers)

for num in numbers:
    if numbers.count(num) >1:
        numbers.remove(num)
numbers.sort()

print(numbers)