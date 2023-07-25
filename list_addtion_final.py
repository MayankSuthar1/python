def addition(lists,que):
    answer = []
    print("---start list---",lists)
    print("---Question---",que)
    j = 0
    for i in lists:
        if(i != None):
            temp = que - i
            if temp in lists:
                answer.append((i,temp))
                lists[lists.index(temp)] = None
                lists[lists.index(i)] = None    
    return answer

lists = [1,2,3,4,5,6,7,8,8,1]
que = 9
print("---Answer---",addition(lists,que))
