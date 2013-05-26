# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    dicts = {}
    
    inputFile = open(filename)
    for line in inputFile:
        line = line.strip('\n')
        tuple1 = line.split(',')
        #print tuple1
        #tuple1[0] = float(tuple1[0])
        tuple1[1] = int(tuple1[1])
        tuple1[2] = int(tuple1[2])
        dicts[tuple1[0]]=(tuple1[1],tuple1[2])

    return dicts        

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

##Debugging code
    
##subjects = loadSubjects('subjects.txt')
##printSubjects(subjects)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    selected = {}
    subjects1 = subjects.copy()
    i = 0
    work_done = 0

    while work_done < maxWork:

        sub = subjects1.copy()
       
        ##The following loop will find out the best of all the keys present
        

        while len(sub)>1:

            for key1 in sub:
                for key2 in sub:
                    if key1 != key2:                    
                        if not comparator(sub[key1],sub[key2]):
                            
                            del sub[key1]
                            break
                        
                if sub.get(key1,-1) == -1:
                    break
        


        ##key2 is the key to the next best element. after checking if the work is better or not we can add it to selected

        if work_done + subjects[key2][WORK]<=maxWork:
            selected[key2] = subjects[key2]
            del subjects1[key2]   ##as it has been selected it must now be deleted
            work_done += subjects[key2][WORK]
            i+=1
            

        else:
            return selected

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """

    subjects = loadSubjects('subjects.txt')

    import time
    

    print
    print 'calling brute force advisor with maxWork = 2'
    maxWork = 2
    start = time.time()
    selected = bruteForceAdvisor(subjects,maxWork)
    stop = time.time()
    time_taken = stop - start
    print 'time taken is: ',time_taken
    print

    print
    print 'calling brute force advisor with maxWork = 3'
    maxWork = 3
    start = time.time()
    selected = bruteForceAdvisor(subjects,maxWork)
    stop = time.time()
    time_taken = stop - start
    print 'time taken is: ',time_taken
    print

    print
    print 'calling brute force advisor with maxWork = 4'
    maxWork = 4
    start = time.time()
    selected = bruteForceAdvisor(subjects,maxWork)
    stop = time.time()
    time_taken = stop - start
    print 'time taken is: ',time_taken
    print

    print
    print 'calling brute force advisor with maxWork = 5'
    maxWork = 5
    start = time.time()
    selected = bruteForceAdvisor(subjects,maxWork)
    stop = time.time()
    time_taken = stop - start
    print 'time taken is: ',time_taken
    print

    print
    print 'calling brute force advisor with maxWork = 6'
    maxWork = 6
    start = time.time()
    selected = bruteForceAdvisor(subjects,maxWork)
    stop = time.time()
    time_taken = stop - start
    print 'time taken is: ',time_taken
    print

    maxWork += 1
    print
    print 'calling brute force advisor with maxWork = ',maxWork
    start = time.time()
    selected = bruteForceAdvisor(subjects,maxWork)
    stop = time.time()
    time_taken = stop - start
    print 'time taken is: ',time_taken
    print

    maxWork += 1
    print
    print 'calling brute force advisor with maxWork = ',maxWork
    start = time.time()
    selected = bruteForceAdvisor(subjects,maxWork)
    stop = time.time()
    time_taken = stop - start
    print 'time taken is: ',time_taken
    print


    maxWork += 1
    print
    print 'calling brute force advisor with maxWork = ',maxWork
    start = time.time()
    selected = bruteForceAdvisor(subjects,maxWork)
    stop = time.time()
    time_taken = stop - start
    print 'time taken is: ',time_taken
    print


##Comments on the time taken:
##    
##on running the function with values of maxWork ranging from 2 to 11
##i found that from 2 to 7 it takes under 4 seconds
##
##whereas at 8 it takes almost 10 seconds and at 9 almost half a minute
##and at 10 it  takes 66 seconds. and at 11 it takes a whopping 166 seconds
##to run!!! and i believe that time taken more than one
##minute is quite unreasonable for a program to run.
##
##so upto max work of 10 this function may work but after 10 it takes an
##unreasonable amount of time

##debugging code
bruteForceTime()

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """

    #TO DO... 

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
