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
    y = 0
    x = 0
    while(x!=-1):
        x=find(target,key,y)
        if(x==-1):
            print 'Number of times that ', key,' appears in ',target0, 'is:',instances
            return instances

        else:
            instances+=1
            y = x+1

    return None

##def countSubStringMatchRecursive(target,key):
##
##    instances = 0
##    y=find(target,key)
##    if(y==-1):
##        print instances
##        return False
##    else:
##        if(countSubStringMatchRecursive(target[(y+len(target)):],key)):
##            instances+=1
##        return True

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
            
            y = x+1
            i+=1
