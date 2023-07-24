def addtion(list,que):

    temp_list = set()
    answer =[]
    
    for i in list:
        
        temp = que - i
        if temp in temp_list:
            answer.append((i,temp))
        temp_list.add(i)
    return answer


list = [1,2,3,4,5,6,7,8]
que = 9
    
print(addtion(list,que))



