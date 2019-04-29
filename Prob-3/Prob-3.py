# Module 2
#   Programming Assignment 2
#     Prob-3.py

# Joel Halnan

def example():
    print("\nExample Output")

    # print a blank line
    print()

    # create three variables and assign three values in a single statement
    v1, v2, v3 = 21, 12.34, "hello"

    # print the variables
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)


def studentCode():
    # replace <name> with your name
    print("\nJoel's Output")
    
    # print a blank line
    print()

    # replicate the assignment statement above, but use your own variable
    # names and values
    var1, var2, var3 = 42, 47, "okay"
    # print the values of the 3 variables
    print("My first variable:\t", var1)
    print("My second variable:\t", var2)
    print("My third variable:\t", var3)
    print()   
    # Get 3 values from the user and assign them to the variables defined
    # above. See the page in Canvas on Simulataneous Assignment
    # BONUS POINTS for using the split() method
    var1, var2, var3 = input("Enter 3 values separated by a space: ").split()
    print("Your first variable:\t", var1)
    print("Your second variable:\t", var2)
    print("Your third variable:\t", var3)
    print()


example()
studentCode()

