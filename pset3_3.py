from string import *

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def countSubStringMatch(target,key):

    """counts the number of times that the key appears in the target"""
         
    target0 = target
    instances = 0
    x = 0
    y = 0
    while(x!=-1):
        x=find(target,key,y)
        if(x==-1):
            print 'Number of times that ', key,' appears in ',target0, 'is:',instances
            return instances

        else:
            instances+=1
            y=x

    return None

def countSubStringMatchRecursive(target,key,x,i):

    
    y=find(target,key,x)
    if(y==-1):
        print 'Number of times that ', key,' appears in ',target, 'is:',i
        return i
    
    else:
        i+=1
        countSubStringMatchRecursive(target,key,y+1,i)
        

def subStringMatchExact(target,key):

    """returns a tuple of all the starting points of the key in the target"""

    start = ()

    y = 0
    x = 0
    i = 0 ##takes care that the indexing is as per the previous orginal target and not as per shortened target
    while(x!=-1):
        x=find(target,key,y)
        if(x==-1):
            
            print 'Tuple of all starting indexes when indicing starts from 0 is:',start
            
            return start

        else:
            start = start +(x,)
            
            y=x+1
            
            i+=1

    return None

def constrainedMatchPair(start1,start2,l1):

    """it returns the tuple of starting points of one substitution where start1 and start2 are the
        the tuples containing the tuples of these two parts of the key"""

    allmatched = ()
    i = 0
    j = 0

    while(i<len(start1)):
        j = 0
        while(j<len(start2)):
            if start1[i] + l1 + 1 == start2[j]:
                allmatched+=(start1[i],)
            j+=1
        i+=1


    print 'The tuple of values with one or no substitution is:',allmatched
    return allmatched

start1 = subStringMatchExact(target1,'a')
start2 = subStringMatchExact(target1,'g')

constrainedMatchPair(start1,start2,1)

subStringMatchExact(target1,'atg')
