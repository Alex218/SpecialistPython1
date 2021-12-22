fruits = ["яблоко", "банан", "киви", "арбуз", "джаботикаба"]
max_length = 0

for i in fruits:
    if len(i) > max_length:
        max_length = (len(i))

for i,fruit in enumerate(fruits,1):
    print(i, ' '*(max_length-len(fruit)), fruit)
