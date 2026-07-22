numbers = [10, 20, 30, 40, 50]
#second larges number from the list
largest=float("-inf")
second_largest=float("-inf")

for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print(second_largest)