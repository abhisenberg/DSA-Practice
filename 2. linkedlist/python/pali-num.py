def blah(x):
    tens = 1
    while x//tens > 9:
        tens *= 10

    #Construct new number
    y, z = 0, x
    while z > 0 :
        digit = z % 10
        y += tens * digit
        tens //= 10
        z //= 10

    print(y)

blah(121)
blah(121735)
blah(6)