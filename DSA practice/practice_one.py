# sum of all prime numbers between 2 and 20

number_list = []
for x in range(3, 20):
    for i in range(2, int(x/2)+1):
        if (x % i) == 0:
            break
    else:
        print(x)
        number_list.append(x)


print(sum(number_list))
