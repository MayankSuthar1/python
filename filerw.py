with open("myfiel.txt",'w+') as f:
    a = input("Plzz enter the data you want to add in the file:-\n")
    if f.write(a):
     print("data inseted")
    f.close()

    print("\n")

    f = open("myfiel.txt",'r+')
    print("you have added this data to your file:-\n")
    print(f.read())
    f.close()




    