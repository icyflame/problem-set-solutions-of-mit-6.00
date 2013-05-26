##problem set 1
##to print the thousnadth prime number

no=1
i=2
j=3
flag=0

while(no!=1000):
    flag=0
    i=2
    for i in range(2,j):
        if(j%i==0):
            flag=1
            break
        i+=1

    if(flag==1):
        print j,' is not prime'
        
    else:
        print j, 'is  prime'
        no+=1

    j+=1

print j-1, ' is thousandth prime'
