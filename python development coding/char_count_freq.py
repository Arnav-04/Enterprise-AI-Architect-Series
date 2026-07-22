s=input()

frequency={}
for char in s:
    frequency[char]=frequency.get(char,0)+1
    
print(frequency)