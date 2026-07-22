#Write Python code to count the frequency of each number and store the result in a dictionary.
numbers = [10, 20, 10, 30, 20, 40, 10]
frequency={}
for num in numbers:
    frequency[num]=frequency.get(num,0)+1
    
print(frequency)