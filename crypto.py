def encryption():

    message = input("Enter the message you want to perform cryptography on :- \n")
    key = int(input("Insert the key for encryption :- "))

    message_rev = message[::-1]
    ascii_value = None
    ciphertext = ""


    for i in message_rev:
        ascii_value =  ord(i)
        
        
        ciphertext = ciphertext+chr(ascii_value+key)
       
    
    print("This is your ciphertext :- '",ciphertext,"'")



def decryption():

    message = input("Enter the message you want to perform decryption on :- \n")
    key = int(input("Insert the key for encryption :- "))

    message_rev = message[::-1]
    ascii_value = None
    ciphertext = ""


    for i in message_rev:
        ascii_value =  ord(i)
        
        
        ciphertext = ciphertext+chr(ascii_value-key)
       
    
    print("This is your message is :- '",ciphertext,"'")




if __name__ == "__main__":
    choose =  str(input("""Hello there are two mode 
Press 1 for encryption
Press 2 for decryption 
:- """))
    match choose:

        case "1":
             encryption()
        case "2":
            decryption()