fruits = ["яблоко", "банан", "киви", "арбуз"]
max_length = 0

for i in fruits:
    if len(i) > max_length:
        max_length = (len(i))

for i in fruits:
    print(' '*(max_length-len(i)), i)
