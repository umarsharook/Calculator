print("""
     .---------------------.
    |  _________________  |
    | |               0 | |
    | |_________________| |
    |  _______________    |
    | |  7 |  8 |  9 | + |
    | |____|____|____|___|
    | |  4 |  5 |  6 | - |
    | |____|____|____|___|
    | |  1 |  2 |  3 | x |
    | |____|____|____|___|
    | |       0       | ÷ |
    | |_______________|___|
    |_____________________|
""")

number1=int(input("Enter the first number\t"))
number2=int(input("Enter the second number\t"))
print("***The operetors***\n Addition-      '+'\n Subtraction-   '-'\n Multiplaction- '*'\n Division-      '/'\n Floor Division-'//'\n Modulo-        '%'\n Power-         '**'\n")
operator=input("Enter the operation that need to perform\t")
if operator=='+':
    print("The sum of first and second number is",number1+number2) #Addition
elif operator=='-':
    print("The subtraction of first and second number is",number1-number2) #Subtraction
elif operator=='*':
    print("The product of of first and second number is",number1*number2) #Multiplaction
elif operator=='/':
    print("The division of first and second number is",number1/number2) #Division
elif operator=='//':
    print("The floor division of first and second number is",number1//number2) #Floor Divide
elif operator=='%':
    print("The modulous of first and second number is",number1%number2) #Modulo
elif operator=='**':
    print("The power of first and second number is",number1**number2) #Power
else:
    print("Enter the valid operation with valid integers") #Invalid Message
