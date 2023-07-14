# simple calculator

#global val1, val2, operator

val1 = int(input("enter your value for first number :- "))
val2 = int(input("enter your value for second number :- "))

operator = input(
    "enter the operator that want do operation \n for '+' press 1 \n for '-' press 2 \n for '*' press 3 \n for '/' press 4 \n ")


class myclss:

    def op():

        match operator:
            case "1":
                return "your output value is :- "+str(val1+val2)
            case "2":
                return "your output value is :- "+str(+val1-val2)
            case "3":
                return "your output value is :- "+str(+val1*val2)
            case "4":
                return "your output value is :- "+str(+val1*val2)
            case _:
                return "plz enter some value"


print(myclss.op())
