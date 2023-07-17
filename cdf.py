class ab:

    def __init__(self):
        i = 0
        i += 1
        print("constructor called "+str(i))

    def __del__(self):
        print("destructor is called")


obj = ab()

print("breack")

n = "mayank"
print(n.find("s"))
print(n.index("y"))
print(n.isalpha())
print(n[::-1])