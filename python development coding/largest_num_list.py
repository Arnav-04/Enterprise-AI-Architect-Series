numbers = [10, 20, 30, 40, 50]
#Write Python code to find the second-largest number without using sort() or sorted().
max_first=max(numbers)
min_first=min(numbers)
print(max_first)
for sec in  numbers:
    if sec<max_first:
        print(sec)
        break
