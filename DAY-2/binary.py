#binary
i=1
while i<=5:#no.of rows
    j=1
    while j<=i:
        if j%2==1:
            print("1",end=" ")
        else:
            print("0",end=" ")
        j+=1
    print()
    i+=1