# Problem Set 4
# Name: Siddharth Kannan 
# Collaborators: None
# Time: 

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """

    retirementFund = []

    retirementFund.append(salary * save * 0.01)

    i = 1

    for i in range(1,years,1):
        retirementFund.append(retirementFund[i-1]+(retirementFund[i-1]*growthRate*0.01)+ salary * save *0.01)

    return retirementFund
        
        
    

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

    retirementFund = []

    retirementFund.append(salary*save*0.01)

    for i in range(1,len(growthRates),1):
        retirementFund.append((retirementFund[i-1]+(retirementFund[i-1]*growthRates[i-1]*0.01)+salary*save*0.01))

    return retirementFund

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """

    funds = []
    funds.append(savings + savings * 0.01 * growthRates[0] - expenses)

    for i in range(1,len(growthRates),1):
        funds.append(funds[i-1] + funds[i-1] * 0.01 * growthRates[i] - expenses)
        

    return funds

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """

    fundsAfterRetirement = nestEggVariable(salary, save, preRetireGrowthRates)

    savings = fundsAfterRetirement[-1] ##cash on the year retired. initial savings

    low = 0
    high = savings
    mid = (low+high)/2.0
    savingsAtTheEnd = epsilon
    i = 0

    while 1:    ##condition for termination of loop is inside the loop and not here

        i+=1
        mid = (low+high)/2.0

        funds = postRetirement(savings,postRetireGrowthRates,mid)

        print 'Iteration:',i,' Expenses:',mid,' Savings on the last day:', savingsAtTheEnd

        savingsAtTheEnd = funds[-1]

        if abs(savingsAtTheEnd)<epsilon:
            return mid

        if savingsAtTheEnd<0:
            high=mid

        else: low=mid

    return mid
    

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = 0.01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.


##testFindMaxExpenses()
