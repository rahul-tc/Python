#Wap to display a Person name, age and address in 3 different lines.
Name = input("Enter the name: ")
Age = int(input("Enter the age: "))
Address = input("Enter the address: ")
print(Name)
print(Age)
print(Address)
#wap to swap two variables.
Vara = "Tejeswee"
Varb = "roushan"

temp = Vara
Vara = Varb
Varb = temp

print(Vara) 
print(Varb)
#wap to convert a float into integer.
Num = float(input("Enter the number : "))
print(int(Num))
#wap to take details from a student for ID-Card and then print it in different Lines.
Name = input("Enter the Name : ")
Batch = input("Enter the Batch : ")
Roll = input("Enter the Roll : ")
print(Name)
print(Batch)
print(Roll)
#wap to take an user i/p as integer then convert it into Float.
user_input = input("Enter an integer: ")
integer_value = int(user_input)
float_value = float(integer_value)
print("The float value is:", float_value)
#wap to check if a number is Positive.
user_input = int(input("Enter a Number : "))
if user_input > 0:
    print("Positive")
else:
    print("Negative")
#wap to check whether a number is odd or even.
user_input = int(input("Enter the number : "))
if user_input%2 == 0:
    print("Even")
else:
    print("Odd")
#wap to create area calculator.
def area_rectangle(length, width):
    return length*width
def area_triangle(base,height):
    return 0.5*base*height
def area_circle(radius):
    import math
    return math.pi*radius**2 #here pi*radius**2 means pir square
def area_square(side):
    return side*side

def main():
    print("Area Calculator")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Square")

    choice = input("Choose a shape (1/2/3/4): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("The area of the rectangle is: ", area_rectangle(length,width))

    if choice == '2':
        base = float(input("Enter the height of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print("The area of the triangle is : ", area_triangle(base,height))

    if choice == '3':
        radius = float(input("Enter the radius of the circle : "))
        print("The area of the circle is: ", area_circle(radius))

    if choice == '4':
        side = float(input('Enter the side of the square : '))
        print("The area of the square is : ",area_square(side))

if __name__ == "__main__":
    main()
#wap to check whether the passed letter is vowel or not.
user_input = input("Enter the Alphabet : ")
if user_input == "a":
    print("Vowel")
elif user_input == "e":
    print("Vowel")
elif user_input == "i":
    print("Vowel")
elif user_input == "o":
    print("Vowel")
elif user_input == "u":
    print("Vowel")
else:
    print("Not Vowel")
#wap to check if a number is a single digit number,2 digit number & so on upto 5 digits.
def check_digit_count(number):
    if number < 0:
        number = -number #convert to positive for checking
    if 0 <= number <10:
        return "Single-Digit number"
    elif 10<= number <100:
        return "Double-Digit Number"
    elif 100<= number <1000:
        return "Three-Digit Number"
    elif 1000<= number <10000:
        return "Four-Digit Number"
    elif 10000<= number <100000:
        return "FIve-Digit Number"

num = int(input("Enter the Number : "))
result = check_digit_count(num)
print(result)

#wap to find a sum of all the even number up to 50.
def sum_of_total_num(limit):
    total = 0
    for num in range(2, limit + 1, 2):
        total +=num
    return total
num = int(input("Enter the Number: "))
result = sum_of_total_num(num)
print(result)

#wap to write first 20 number and their squared number.
def print_square(limit):
    for num in range(1, limit+1):
        square = num * num
        print(f"The Number is {num} and the square is : {square} ")
    
number = int(input("Enter the number : "))
result = print_square(number)
print(result)

#wap to find sum of first 10 odd numbers using while loop.
def odd_numbers(limit):
    total = 0
    num = 1
    while num <= limit:
        total += num
        num += 2
    return total

num = int(input("Enter the Number: "))
result = odd_numbers(num)
print(result)

#wap to check if a number is divisible by 8 and 12, upto 100 Numbers.
def check_divisible(number):
    if number%8 == 0:
        return "Divisble by 8"
    elif number%12 == 0:
        return "Divisble by 12"
    else:
        return "Not divisble by 8 and 12"
num = int(input("Enter the number : "))
result = check_divisible(num)
print(result)

#wap to create a billing system at supermarket.
while True:
    name = input("Enter the Customer Name : ")
    total = 0

    while True:
        #print("Enter the Amount and Quantity : ")
        amount = float(input("Enter Amount : "))
        Quantity = float(input("Enter the Quantity : "))
        total += amount*Quantity
        repeat = input("Do you want to add more items ? Yes/No : ")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name :", name)
    print("Amount to be paid :", total)
    print("-"*40)
    print("************Happy Shopping*************")

    repeat1 = input("do you want to go to next customer ? Yes/No :")
    if repeat1 == 'no' or repeat1 == "No":
        break
        
#Fourth Set
# A = "Why Fit in, When you are Born to Stand out !"
#wap to find the length of the following string.
#wap to check how many time alphabet o is occuring.
#wap to convert the whole string into lower & upper Case.
#wap to convert the following string into a title.
#wap to find the index number of "Fit in".
#Patterns
"""
1
12
123
1234
12345
"""
"""
1
22
333
4444
55555
"""
"""
11111
2222
333
44
5
"""
"""
*****
****
***
**
*
"""
"""
   *
  **
 ***
****
"""
"""
1
21
321
4321
54321
"""
"""
*
**
***
****
***
**
*
"""
"""
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
"""
#Fifth Set
#Wap to get Fibonaaci Series up to 10 numbers.
#wap to check if a number is prime or not.
#wap to find a palindrome of integers.
#wap to create an area calculator.
#sixth Set
#A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
#wap to separate the following string into comma(,) separated values.
#wap to sort string alphabetacilly in python.
#wap to remove a given character from a string.


