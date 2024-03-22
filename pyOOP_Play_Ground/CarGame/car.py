import sys
import argparse
import math

""" This Class was created to simulate the position and direction a car is in/heading towards.

    Attributes:
    x: The current x position of the car.
    y: The current y position of the car.
    heading: The direction the car is pointing towards.
    This value is given in degrees, where 0 is pointed north, 90 is pointed east, etc.
"""
class Car:

    """Initializes an instance of a Car. Takes 3 optional inputs.
        Args:
        x (float): x position of the car. Default is set to 0.
        y (float): y position of the car. Default is set to 0.
        heading (float): Direction the car is heading in, given in degrees. Default is set to 0.

        Side Effects:
        If the user creates an Car instance with optional parameters filled in, those values will
        override the initial values of 0, 0, 0 and will be used in context for calculations with 
        the turn() and drive() methods.
    
    """  
    def __init__(self, x=0, y=0, heading=0):
        #validates input parameters and sets initial position and heading of the car
        self.x = x
        self.y = y
        self.heading = heading
    
    """ Define a method that takes self and number of degrees to determine how and in which the direction will turn

        Args: 
        self (Car): The current instance of the object
        degrees (float): degrees to turn the car by
    """
    def turn(self, degrees):
        #Adds the degrees to the current heading
        self.heading += degrees
        
        #Ensures the heading stays within the range of 0-360 degrees
        while (self.heading < 0): 
            self.heading += 360
        self.heading %= 360 #normalizes the heading so it is 0-360

    """Define a method that takes self and distance to determine the distance the car travels

        Args:
        self (Car): The current instance of the object
        distance (float): The distance the user wants the car to travel

    """
    def drive(self, distance):
        #Calculates the change in x and y coordinates based on the heading and distance 
        addx = distance*math.sin(math.radians(self.heading))
        suby = distance*math.cos(math.radians(self.heading))
        #Updates the car's position
        self.x += addx
        self.y -= suby

"""Define a function that gives car directions and finds the location

Args: None
Returns: Location and heading of the car
"""
def sanity_check():
    # Creates a new instance of the car class
    car1 = Car()

    #Sets the inital position and heading of the car
    car1.x = 0
    car1.y = 0
    car1.heading = 0

    #turns the car 90 degrees to the right
    car1.turn(90)
    #moves the car forward 10 units
    car1.drive(10)
    #move the car 30 degrees to the right
    car1.turn(30)
    #moves the car forward 20 units
    car1.drive(20)
    #prints the car's current location
    print("Location: " + str(car1.x) + ", " + str(car1.y))
    #prints the car's current heading
    print("Heading: " + str(car1.heading))
    #returns the created car object
    return car1



def main(parameter1, parameter2):
    pass

def parse_args(args_list):
    
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operations commence. 
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    
    parser.add_argument('required', type=float, help='This is an example of a required argument.')
    parser.add_argument('--optional', '-o', type=int, default=12, help='This is an example of an optional argument')  
    
    args = parser.parse_args(args_list) #We need to parse the list of command line arguments using this object.

    return args

if __name__ == "__main__":
    
    sanity_check()