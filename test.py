a = range(1,101)
for i in a:
    if i%7 == 0 or i%10 == 7 or int(i/10) == 7:
        continue
    else:
        print(i)
