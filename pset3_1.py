from string import *

def countSubStringMatch(target,key):

    """counts the number of times that the key appears in the target"""

    target0 = target
    instances = 0
    y = 0
    x = 0
    while(x!=-1):
        x = find(target,key,y)
        if(x==-1):
            print 'Number of times that ', key,' appears in ',target0, 'is:',instances
            return instances

        else:
            instances+=1
            y=x+1
            ##target=target[(x+len(key)):]

    return None
            


def countSubStringMatchRecursive(target,key,x,i):

    
    y=find(target,key,x)
    if(y==-1):
        print 'Number of times that ', key,' appears in ',target, 'is:',i
        return i
    
    else:
        i+=1
        countSubStringMatchRecursive(target,key,y+1,i)
        


p = input('Enter the target string:')
q = input('Enter the key string:')

p = 'atcgtagcta'
q = 'a'

i = 0

countSubStringMatch(p,q)
countSubStringMatchRecursive(p,q,0,i)
