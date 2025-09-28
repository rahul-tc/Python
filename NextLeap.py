#1 - Printing "Hello World"
class Solution:
    def helloWorld(self):
        # Your code goes here
        print("Hello World")

#2 - Print Two Lines
class Solution:
	def printTwoLines(self):
		print("Hello there!")
		print("Let's start")
		
#3 - String to Boolean
class Solution:
	def stringToBoolean(self, str: str) -> bool:
		return str.lower() == "true"

#4 - Integer to string
class Solution:
    def intToString(self, num: int) -> str:
        # Convert integer to string using str() function
        return str(num)

#5 - Add Two Numbers
class Solution:
    def addTwoNumbers(self, a: int, b: int) -> int:
        # Your code goes here
        return a + b

#6 - Multiplying Numbers
class Solution:
    def multiplyTwoNumbers(self, a: int, b: int) -> int:
        # Your code goes here
        return a * b

#7 - Calculate area of Circle
import math

class Solution:
	def calculateCircleArea(self, r: float) -> float:
        return math.pi * r * r
	
#8 - Checking Value Inequality
class Solution:
	def checkNotEqual(self, a: int, b: int) -> bool:
	    if a != b:
	        return true
	    else:
	        return false

#9 - Checking Value Equality
class Solution:
    def checkSameValue(self, a: int, b: int) -> bool:
        # Your code goes here
        if a == b:
            return True
        else:  
            return False	
