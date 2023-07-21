list = [1,2,3,4,5,6,7,8]
question = 9
answer = []


def two_digit():

    for i in list:

        for a in range(list[0], i+1):

            if (i + a == question):
                
                temp_tuple = (a, i)
                answer.insert(len(answer), temp_tuple)
        
        for b in range(i+1):
            for temp in range(list[0], b+1):
                # print(temp)
                if (i + b + temp == question):
                    if (i != b and i != temp and b != i and b != temp and temp != i and temp != b):
  
                        temp_tuple = (temp, b, i)
                        answer.insert(len(answer), temp_tuple)
        
        for c in range(i+1):
                for temp in range(list[0], c+1):
                     for temp1 in range(list[0], temp+1):
                          
                        if (i+c+temp+temp1 == question):
                            if(i!=c and i!=temp and i!=temp1 and c!=i and c!=temp and c!=temp and temp!=i and temp!=c and temp!=temp1 and temp1!=i and temp1!=c and temp1!=temp):

                                
                                temp_tuple = (i , c , temp ,temp1)
                                answer.insert(len(answer), temp_tuple)
     

    print(answer)


two_digit()
 
 