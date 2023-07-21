insert_searching_value = int(input("Enter a value from 1 to 100 which you want to search :- "))

list = [39,67,80,76,17,77,81,57,25,54,31,36,75,56,19,3,46,43,64,30,5,72,85,55,79,51,71,28,73,48,37,95,2,8,35,44,26,82,27,90,66,100,10,20,98,29,58,49,41,84,52,22,89,24,18,4,6,88,1,87,91,42,99,33,83,61,16,21,68,13,34,86,60,32,23,65,74,63,11,96,70,47,94,40,69,50,62,12,45,93,9,59,14,38,7,78,15,97,53,92]

sorted_list = sorted(list)






def searching(list_for_searching , searching_value):
   
   size = len(list_for_searching)

   if(size % 2 == 0):

      # this below 3 variable will use to find the center of the list
      center1  = int(size / 2)
      center2  = int((size / 2) + 1)
      average = (center1 + center2)/2

      if(searching_value == list_for_searching[center1]):

         print("Yes! the value has be found and its index No. is := ", list_for_searching.index(list_for_searching[center1]))

      elif(searching_value == list_for_searching[center2-1]):

         print("Yes! the value has be found and its index No. is := ", list_for_searching.index(list_for_searching[center2-1]))

      elif (searching_value < average):

        for i in range(list_for_searching[int(average)]):
           
           if (searching_value == list_for_searching[i]):
              print("Yes! the value has be found and its index No. is := ", list_for_searching.index(list_for_searching[i]))

      elif (searching_value > average):

        for i in range(list_for_searching[int(average)],list_for_searching[len(list_for_searching)-1]):
           if (searching_value == list_for_searching[i]):
              print("Yes! the value has be found and its index No. is := ",list_for_searching.index(list_for_searching[i]))
      
      else:
         print("There is no such value to found in the list that you have given")
   

   else:
      
      center = size//2

      if(searching_value == list_for_searching[center]):

         print("Yes! the value has be found and its index No. is := ", list_for_searching.index(list_for_searching[center]))

      elif(searching_value < list_for_searching[center]):

          for i in range(list_for_searching[center]):
           
           if (searching_value == list_for_searching[i]):
              print("Yes! the value has be found and its index No. is := ", list_for_searching.index(list_for_searching[i]))

      elif(searching_value > list_for_searching[center]):

         for i in range(list_for_searching[center],list_for_searching[len(list_for_searching)-1]):
           
            if (searching_value == list_for_searching[i]):
              print("Yes! the value has be found and its index No. is := ", list_for_searching.index(list_for_searching[i]))

      else:
         print("There is no such value to found in the list that you have given")
      
         




#if(insert_searching_value >= 1 and insert_searching_value <= 100):
searching(sorted_list,insert_searching_value)



