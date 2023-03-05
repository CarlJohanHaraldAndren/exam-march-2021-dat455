"""

Question 1
The martian year has 668.5907 sols, so just like on Earth, the martian
calendar has leap years. A leap year is a year which is odd or divisible
by ten. The leap year has 669 sols, while a normal year has 668. Write a
program which asks the user for a year and prints out its length in days.
The following are three example dialogs:
Enter a martian year: 189
Year 189 has 669 sols
Enter a martian year: 218
Year 218 has 668 sols
Enter a martian year: 220
Year 220 has 669 sols

"""

def martian():
    year=int(input('Entar a martian year: '))

    if year%10==0 or year%2!=0:
        print("Year " + str(year) + " has 669 sols")
    else:
        print("Year " + str(year) + " has 668 sols")

martian()