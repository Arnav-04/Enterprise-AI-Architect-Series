population = {
    "Noida": 5000000,
    "Delhi": 600000,
    "Gurgaon": 4500000,
    "Mumbai": 8000000
}

threshold = 3500000

#cities which are having the population greater than the threshold and store it new dictionary
field_population={}
for city,pop in population.items():
    print(city)
    print(pop)
    if pop> threshold:
        field_population[city]=pop

print(field_population)