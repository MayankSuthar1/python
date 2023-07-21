def encryption():

    message = input("Enter the message you want to perform cryptography on :- \n")
    key = int(input("Insert the key for encryption :- "))

    message_rev = message[::-1]
    ascii_value = None
    ciphertext = ""


    for i in message_rev:
        ascii_value =  ord(i)
        
        
        ciphertext = chr(ascii_value+key)
       
    
    print(ciphertext)

encryption()