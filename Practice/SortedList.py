#  Print without duplicates

#from collections import Count

list1 = [21.54,45,65,54,56,54,65,76,8,9,65,32,43,12,21]

list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)
        

print("List2: ",list2)


print("Sorted List2: ",sorted(list2))


        
    
