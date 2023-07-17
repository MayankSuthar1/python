'''def cal(a,b=10):
    
    return print(a+b)

cal(10,20)'''

def ave(*number):
    sum = 0
    for i in number:
        sum = sum+i
    print("the average of your numbers is :- "+str(sum/len(number)) )

ave(1,2,3,4,5,6,7,8,9)

def fn(**fns):
    print("hello", fns["sname"], fns["name"], fns["lname"])

fn(name="Mayank",sname="Suthar",lname="RajendraKumar")