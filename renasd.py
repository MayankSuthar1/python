import os

f = os.listdir("data/")
d = len(f)

a = 100



for i in f:
    
    
    a-=1
    os.rename(f"data/{i}", f"data/{a}.png")
    
