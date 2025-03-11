for i in range(2,101):   # The range() function does not include the last number (the ending number). Only numbers from 2 to 100 are counted.
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")