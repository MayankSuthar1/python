import os
print(dir(os))

class cc:
    def __init__(self):
        d = "called"
        print(d)

    def __del__(self):
        c = "hello"
        print(c)


cc()

