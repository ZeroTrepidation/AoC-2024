from src.solutions import day1Solution, day2Solution, day3Solution



# Defining main function
def main():
    print("Welcome to my Advent of Code Program")

    day = input("What day's solution would you like to view?\n\n")

    if int(day) == 1:
        print(day1Solution.solution())
    elif int(day) == 2:
        print(day2Solution.solution())
    elif int(day) == 3:
        print(day3Solution.solution())
    else:
        print("Invalid day selection")


# Using the special variable
# __name__
if __name__=="__main__":
    main()