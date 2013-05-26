# Problem Set 11: Simulating robots
# Name: Siddharth Kannan
# Collaborators: None
# Time:

import math
import random
import ps11_visualize
#import pylab

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
        self.w = width
        self.h = height

        self.noOfCleanedTiles = 0

        self.cleanedTiles = [] #A list that will store the positions of all the cleaned tiles
        
        
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        correct(pos)

        self.cleanedTiles.append(pos)

        self.noOfCleanedTiles += 1

        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """

        for i in self.cleanedTiles:
            if i.getX() == m and i.getY() == n:
                return True

        return False
        
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return float(self.w * self.h)
    
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return float(self.noOfCleanedTiles)
    
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """

        listX = range(self.w)

        listY = range(self.h)

        x = random.choice(listX)
        y = random.choice(listY)

        return Position(x,y)


        
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """

        return ((pos.x < self.w) and (pos.y < self.h) and pos.x >= 0 and pos.y >=0)


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

        self.room = room
        self.speed = speed
        self.p = room.getRandomPosition()
        self.d = random.choice(range(360))
        
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
        
        self.p.x = position.getX()
        self.p.y = position.getY()

        correct(self.p)
        
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """

        self.d = direction

##Helper functions

def correct(p):
    """p is a position object

        this function will make the position of it integers"""

    p.x = int(p.x)
    p.y = int(p.y)

    return p

def hitAWall(currentPos,angle,width,height):
    """Function that returns a boolean depending on whether it will hit
        a wall or not"""

    w = width
    h = height
    x = currentPos.x
    y = currentPos.y

    leftWall = angle>=225 and angle<=315
    rightWall = angle>=45 and angle<=135
    upWall = (angle>=315 and angle<=360) or (angle>=0 and angle<=45)
    downWall = angle>=135 and angle<=225

    if ((x == 0 and leftWall) or \
       (x == w-1 and rightWall) or \
       (y == 0 and downWall) or \
       (y == h-1 and upWall)):

        return True

    else:
        return False

def calCorNewPosition(direction,speed,currentPos,w,h):
    """Returns the next box in the grid"""

    d = direction
    s = speed

    np = Position(0,0)

    angle = direction

    leftWall = angle>225 and angle<315
    rightWall = angle>45 and angle<135
    upWall = (angle>315 and angle<360) or (angle>0 and angle<45)
    downWall = angle>135 and angle<225

    x = currentPos.x
    y = currentPos.y
        
    
    if d == 45:
        x += s
        y += s

    if d == 135:
        x -= s
        y += s

    if d == 225:
        x -= s
        y -= s

    if d == 315:
        x += s
        y -= s

    if upWall:
        y += s

    if downWall:
        y -= s

    if rightWall:
        x += s

    if leftWall:
        x -= s

    np.x = x
    np.y = y

    return np


##angle = 270
##
##
##leftWall = angle>=225 and angle<=315
##rightWall = angle>=45 and angle<=135
##upWall = (angle>=315 and angle<=360) or (angle>=0 and angle<=45)
##downWall = angle>=135 and angle<=225
##
##print 'up:',upWall
##print 'down:',downWall
##print 'left:',leftWall
##print 'right:',rightWall
        


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

##        Pos = self.p
##
##        if self.room.isTileCleaned(Pos.x ,Pos.y):
##            print 'tile at ',Pos.x,',',Pos.y,' was cleaned already'
##
##        else:
##            print 'tile at ',Pos.x,',',Pos.y,' has been cleaned now'
##            
##            self.room.cleanTileAtPosition(Pos)

        d = self.d

        cp = self.p   ##the current position

        np = self.p   ##Where the new position will be stored

        if hitAWall(self.p,self.d,self.room.w,self.room.h):

##            print '------------------------------'
##            print
##            print
##
##            print 'hit a wall branch'
##
##            print 'angle is ',self.d
##
##            print 'position is ',self.p.x,',',self.p.y

            
            while self.room.isPositionInRoom(self.p):
                d = random.choice(range(360))

                #print 'calculated the random direction as:',d

                np = calCorNewPosition(d,self.speed,cp,self.room.w,self.room.h)

                #print 'calculated new position as:',np.x,',',np.y

                if self.room.isPositionInRoom(np):
                    #print 'as it is inside the room we can break out of here'   #and not hitAWall(np,d,self.room.w,self.room.h):
                    break

                #print 'it is not inside the room so we must continue'

        #if not hitAWall(self.p,self.d,self.room.w,self.room.h):

        else:
##
##            print '------------------------------'
##            print
##            print
##
##            print 'did not hit a wall'
##
##            print 'angle is ',self.d
##
##            print 'position is ',self.p.x,',',self.p.y
            
            np = calCorNewPosition(d,self.speed,np,self.room.w,self.room.h)

            while not self.room.isPositionInRoom(np):
                d = random.choice(range(360))

                np = calCorNewPosition(d,self.speed,np,self.room.w,self.room.h)


        self.setRobotPosition(np)

        self.setRobotDirection(d)

        newPos = np        

        if self.room.isTileCleaned(newPos.x ,newPos.y):
            pass
            #print 'tile at ',newPos.x,',',newPos.y,' was cleaned already'

        else:
            #print 'tile at ',newPos.x,',',newPos.y,' has been cleaned now'
            
            self.room.cleanTileAtPosition(newPos)
            


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

    listToBeReturned = []

    listForEachTrial = []

    robots = []

    room = RectangularRoom(width,height)

    cleanedRatio = 0

    for i in range(num_robots):
        a = robot_type(room,speed)
        robots.append(a)

    for i in range(num_trials):

        if visualize:
            anim = ps11_visualize.RobotVisualization(num_robots,width, height)

        epsilon = 0.01

        while abs(cleanedRatio-min_coverage) > epsilon:
                
            for i in range(num_robots):
                robots[i].updatePositionAndClean()            

            cleanedRatio = room.getNumCleanedTiles() / room.getNumTiles()

            print 'amount of room cleaned till now:',cleanedRatio*100,'%'

            listForEachTrial.append(cleanedRatio * 100)

            if visualize:
                anim.update(room, robots)

        if visualize:
            anim.done()

        listToBeReturned.append(listForEachTrial)

    return listToBeReturned


#avg = runSimulation(1, 1.0,10, 10, 0.1, 1, Robot,True)

#avg1 = runSimulation(2,1.0,5,5,1,1,Robot,True)

#avg1 = runSimulation(3,1.0,5,5,1,1,Robot,True)

#avg1 = runSimulation(5,1.0,10,10,1,1,Robot,True)

avg1 = runSimulation(1,1.0,5,5,1,1,Robot,True)

#avg1 = runSimulation(1,2.0,5,5,1.0,1,Robot,True)


##room = RectangularRoom(15,10)
##
##print room.getNumTiles()
##
##
##p = Position(12,9)
##q = Position(0,0)
##r = Position(6,6)
##
##room.cleanTileAtPosition(p)
##print float((room.getNumCleanedTiles() / 150.0))
##room.cleanTileAtPosition(q)
##
##print float((room.getNumCleanedTiles() / room.getNumTiles()))
##
##print room.isTileCleaned(p.x,p.y)
##print room.isTileCleaned(q.x,q.y)
##print room.isTileCleaned(r.x,r.y)
##
##print room.noOfCleanedTiles
##
##print room.getNumCleanedTiles()

##r = Robot(room,1.0)
##
##print r.getRobotDirection()
##
##print r.getRobotPosition()
##
##r.updatePositionAndClean()
##
##print r.getRobotDirection()
##
##print r.getRobotPosition()




# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
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
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here
