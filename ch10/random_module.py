import random

# seed : ensuring same result
# random.seed(47)

animals = ['cat', 'duck', 'dodobird','tiger', 'whale']

print(random.choice(animals))
print(random.sample(animals,2))
print(random.randint(0,5))

for i in range(5):
    print(random.randint(10,53))