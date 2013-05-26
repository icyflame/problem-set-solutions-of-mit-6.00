##problem set 1
##to print the thousnadth prime number

from math import *  ##imports the functions from the math file to use logarithm


i=2
j=2
flag=0
sum1=0

n=input('Enter the number till which you want to go:')

while(j<n+1):
    flag=0
    i=2
    for i in range(2,j):
        if(j%i==0):
            flag=1
        i+=1

    if(flag==0):
        
    ##the number j is prime now add this to sum
        sum1+=log(j)
        print sum1            
    j+=1
    

ratio=1.0
ratio=sum1/n;

print 'n is:',n
print 'sum of logartithms is:',sum1
print 'the ratio of sum:n is:',ratio
