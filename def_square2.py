def model2(n):
    i=0
    while i<n:
        j=0
        while j<n:
            if(i+j)%2==0:
                print(".", end=" ")
            else:
                print("#", end=" ")
            j = j+1
        print()
        i = i+1
        
model2(10)