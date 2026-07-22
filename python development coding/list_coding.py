#question - Create a new list containing only even numbers, with every selected number multiplied by 2.
numbers = [10, 15, 20, 25, 30, 35, 40]
even_number=[x*2 for x in numbers if x%2==0]
print(even_number)