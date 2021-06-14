count = 1

amount = 10

while count <= 10:
    print(count, amount)
    count += 1
    amount += count

    if amount > 30:
        break
else:
    amount += count
    print(count, amount)