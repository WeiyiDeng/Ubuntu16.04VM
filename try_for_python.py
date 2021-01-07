fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

print(enumerate(fruit))

for i,type in enumerate(fruit):
    fruit[i] = fruit[i].replace('a', '!')
    print(i)
print(fruit)

print(len(fruit))

fruit = [f.replace('e', '!') for f in fruit]
print(fruit)
