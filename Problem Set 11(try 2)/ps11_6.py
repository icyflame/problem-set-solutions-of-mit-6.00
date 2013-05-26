# Problem Set 11: Simulating robots
# Name:  Siddharth Kannan
# Collaborators:
# Time:

import math
import ps11_visualize

from pylab import *
# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """

        self.w = width  ##the width of the room
        self.h = height  ##the height of the room

        self.cleanedTiles = []  ##list contains of all the position objects that have been cleaned
        
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """

        assert pos.x >= 0
        assert pos.y >=0

        pos  = Position(math.floor(pos.x),math.floor(pos.y))

        self.cleanedTiles.append(pos)   ##we correct the position so as to get the integers and add that to the cleaned tiles list

        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """

        m = math.floor(m)

        n = math.floor(n)

        m = int(m)
        n = int(n)

        if not type(m)== int or not type(n) == int:

            raise TypeError


        for i in self.cleanedTiles:            

            if i.x == m and i.y == n:


                return True


        return False

    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """

        return (self.w * self.h)
        
        
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """

        hashtile = []  ##will store the tiles that have bee cleaned

        count = 0  ##the total number of cleaned tiles

        for i in self.cleanedTiles:

            if not i in hashtile:  ##if this position has already been counted then it will not be counter again

                count += 1
                hashtile.append(i)

        return count

    
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        import random

        pos = Position(random.choice(range(self.w)),random.choice(range(self.h)))

        return pos

    
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """

        result =  (math.floor(pos.x) < self.w) and (math.floor(pos.y) < self.h) and (math.floor(pos.x) >= 0) and (math.floor(pos.y) >= 0)

        return result


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """

        self.speed = speed  ##the speed with which the robot can move

        self.room = room  ##the room in which the robot is present

        import random

        self.d = random.choice(range(360))  ##the random position in which the robot will move

        self.p = Position(0,0)

        self.p = self.room.getRandomPosition()  ##selects a random position for the robot inside the room

        
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """

        return self.p

    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.d

    
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.p = Position(position.x,position.y)

        
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """

        
        self.d = direction
        

class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        self.p = self.p.getNewPosition(self.d,self.speed)

        if not self.room.isPositionInRoom(self.p):  ##if the position is not in the room

            import random

            ##creating copies of the old position

            old_pos = Position(self.p.x,self.p.y)  ##the old position which will remain fixed

            newPos = Position(self.p.x,self.p.y)  ##the new position generated each time

            while not self.room.isPositionInRoom(newPos):               

                self.d = random.choice(range(360))

                newPos = old_pos.getNewPosition(self.d,self.speed)

                if self.room.isPositionInRoom(newPos):

                    break                

        

            self.p = newPos

        if not self.room.isTileCleaned(self.p.x,self.p.y):

            self.room.cleanTileAtPosition(self.p)                


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """

    listForAllTrials = []

    if visualize:

            anim = ps11_visualize.RobotVisualization(num_robots, width, height)


    for i in range(num_trials):

        ##intiating the room and the robots
        
        room = RectangularRoom(width,height)

        robots = []  ##The list that contains all the robots
        

        for i in range(num_robots):            

                robots.append(robot_type(room,speed))

        ##runs num_trials trials of the simulation

        listForThisTrial = []        

        areaCovered = 0

        epsilon = 0.001

        while areaCovered < min_coverage:

            for i in range(len(robots)):

                robots[i].updatePositionAndClean()

            if visualize:

                anim.update(room, robots)
            
            areaCovered = room.getNumCleanedTiles() / float(room.getNumTiles())                

            listForThisTrial.append(areaCovered)

        if visualize:

            anim.done()

        listForAllTrials.append(listForThisTrial)

    return listForAllTrials

#avg = runSimulation(1,1,5,5,1,300,Robot,False)

#avg1 = runSimulation(13,1,10,10,1,1,Robot,True)

#print avg

# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """

    import pylab
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4

num_trials = 20  ##the number of trials to be run

##helper function for plot 1

def runSimluationOnOneRobotSeventyFivePercent(width,height,rtype=Robot):

    result = runSimulation(1,1,width,height,0.75,num_trials,rtype,False)

    ##now we have to compute the mean time

    meanTime = 0

    for i in result:

        meanTime += len(i)

    meanTime /= len(result)

    return meanTime

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """

    listOfDimensions = [5,10,15,20,25]

    times = []  ##list will store the average time for each of the rooms

    areas = []  ##list will store the areas of each of the rooms

    for i in listOfDimensions:

        times.append(runSimluationOnOneRobotSeventyFivePercent(i,i))

        areas.append(i**2)

    figure()

    plot(areas,times)

    title('Time taken to clean 75% of a square room vs. Area of the room')

    xlabel('Area of the room')

    ylabel('Time taken(by 1 robot)')

    ylim([0,1200])

    xlim([0,650])

    show()

#showPlot1()

##helper functions for plot 2
    

def runSimluationOnPlot2(noOfRobots,rtype=Robot):    

    result = runSimulation(noOfRobots,1,25,25,0.75,num_trials,rtype,False)

    meanTime = 0

    for i in result:

        meanTime += len(i)

    meanTime /= len(result)

    return meanTime

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """

    noOfRobots = range(1,11)

    times = []

    for i in noOfRobots:

        times.append(runSimluationOnPlot2(i))

    figure()

    plot(noOfRobots,times)

    title('Time to clean 75% of a square room vs no of robots')

    xlabel('Number of robots')

    ylabel('Time taken to clean 75% of the room(25 by 25)')

    xlim([0,11])

    ylim([0,1200])

    show()

#showPlot2()

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """

    ##helper function will be same as plot 1

    dimensions = [(20,20),(25,16),(40,10),(50,8),(80,5),(100,4)]

    times = [] ##list that stores the time taken

    ratios = [] ##stores the ratio of the width to the height

    for (i,j) in dimensions:

        times.append(runSimluationOnOneRobotSeventyFivePercent(i,j))

        ratios.append(i / float(j))

    figure()

    plot(ratios,times)

    title('Time to clean 75% of the room vs. Ratio of width to height')

    xlabel('Ratio(width : height)')

    ylabel('Time taken(by one robot)')

    xlim([0,26])

    ylim([500,1200])

    show()

#showPlot3()

##helper functions for plot 4

def runSimPlot4(min_coverage,no_robots,rtype=Robot):

    result = runSimulation(no_robots,1,25,25,min_coverage,num_trials,rtype,False)

    meanTime = 0

    for i in result:

        meanTime += len(i)

    meanTime /= len(result)

    return meanTime
    

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """

    noOfRobots = range(1,6)

    meanTimes = []

    percentages = range(0,101,10)

    for i in noOfRobots:

        print 'for number of robots:',i

        print meanTimes

        meanTimes.append([])

        for areaMin in percentages:

            print 'percentage:',areaMin,'%',

            result = runSimPlot4(areaMin/100.0,i)

            print result,' seconds'

            meanTimes[i-1].append(result)

    figure()

    counter = 1

    for i in meanTimes:

        plot(percentages,i,label= '%s Robots' %counter)

        counter += 1

    title('Time taken to clean the room vs. percentage of the room cleaned')

    xlabel('Percentage of the room cleaned')

    ylabel('Time taken to clean the room')

    xlim([0,102])

    ylim([0,4000])

    legend(loc=2)

    show()    

#showPlot4()    

# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        import random

        self.d = random.choice(range(360))

        self.p = self.p.getNewPosition(self.d,self.speed)

        if not self.room.isPositionInRoom(self.p):  ##if the position is not in the room

            import random

            ##creating copies of the old position

            old_pos = Position(self.p.x,self.p.y)  ##the old position which will remain fixed

            newPos = Position(self.p.x,self.p.y)  ##the new position generated each time

            while not self.room.isPositionInRoom(newPos):               

                self.d = random.choice(range(360))

                newPos = old_pos.getNewPosition(self.d,self.speed)

                if self.room.isPositionInRoom(newPos):

                    break 

            self.p = newPos

        if not self.room.isTileCleaned(self.p.x,self.p.y):

            self.room.cleanTileAtPosition(self.p)
    
#avg1 = runSimulation(2,1,5,5,1,1,RandomWalkRobot,True)

# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """

    ##the time that the two types of robots take to clean a 5 by 5 room


    ##for one robot. time of completion vs room area

    normal = []

    randomWalk = []

    areas = []

    for i in range(1,10):

        print i**2,' square units'

        print 'type normal'        

        normal.append(runSimluationOnOneRobotSeventyFivePercent(i,i,Robot))

        print 'type random'

        randomWalk.append(runSimluationOnOneRobotSeventyFivePercent(i,i,RandomWalkRobot))

        areas.append(i**2)


    figure()

    plot(areas,normal,label='Normal Robot')

    plot(areas,randomWalk,label='Random Walk Robot')

    title('Comparison(robot type vs. room area)')

    xlabel('Area of the room')

    ylabel('Time taken(to clean complete room, 1 robot')

    legend(loc=2)

    show()                         

showPlot5()
