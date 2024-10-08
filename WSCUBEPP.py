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
#Third Set
#wap to find a sum of all the even number up to 50.
#wap to write first 20 number and their squared number.
#wap to find sum of first 10 odd numbers using while loop.
#wap to check if a number is divisible by 8 and 12, upto 100 Numbers.
#wap to create a billing system at supermarket.
#Fourth Set
# A = "Why Fit in, When you are Born to Stand out !"
#wap to find the length of the following string.
#wap to check how many time alphabet o is occuring.
#wap to convert the whole string into lower & upper Case.
#wap to convert the following string into a title.
#wap to find the index number of "Fit in".
