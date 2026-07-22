s = input()
#find first non repeating character
frequency={}

for char in s:
    frequency[char]=frequency.get(char,0)+1

for char in s:
    if frequency[char]==1:
        print(char)
        break