import random


def ran(n):

   # random.seed("mayank")

    for i in range(n):
        a = random.randint(1, 6)
        print(f"you have rolled {i} :- ",a)

def taken():
    global insert
    insert = int(input("how many time you want to roll the dice choose only between 1 to 6 :- "))
    if (insert == 1 or insert == 2 or insert == 3 or insert == 4 or insert == 5 or insert == 6):
       return ran(insert)
    else:
       return taken()


taken()

