#program to code or decode secret code language
import random
import string

def code():
    print("\nYou have choose to code a secret language.")
    c = input("Enter a message to convert into a secret code.\nAnswer : ")
    if len(c) > 3:
        encode1 = ''.join(random.choices(string.ascii_letters, k=3))
        encode2 = ''.join(random.choices(string.ascii_letters, k=3))
        encode3 = encode1 + c[1:] + c[0] + encode2
        print(encode3)
    else:
     print(c[::-1])

def decode():
    print("\nYou have choose to decode a secret language.")
    d = input("Enter a message to decode.\nAnswer : ")
    if len(d) < 3:
        print(d[::-1])
    else:
        decode1 = d[-4] + d[3:-4]
    print(decode1)

while(True):
#asking input from user to whether code or decode
    a = int(
    input(
    "\nWelcome !\nDo you want to code or decode a secret message ?\n1.Code\t2.Decode\t0.Exit\nEnter valid number : "
    ))
    if a == 1:
        code()
    elif a == 2:
     decode()
    elif a == 0:
        print("\nThank you!\tProgram has been exited!")
        break
    else:
        print("\nInvalid Selection !!!")