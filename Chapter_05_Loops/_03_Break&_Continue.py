# BREAK 
i = 0
while i < 10 :
    if (i == 5) :
        print(i)
        break

    print(i)
    i += 1
print("\n")


# CONTINUE 
j = 0
while j <= 10 :
    if (j == 5) :     # (j%2 == 0) even num
        print("skip ")
        j += 1
        continue
    print(j)
    j += 1



