my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#print(my_list)
my_list.insert(2,15)
#print(my_list)
list=[50,60,70]
my_list.extend(list)
#print(my_list)
my_list=my_list[:-1]
#print("new my_list:",my_list)
my_list.sort()
index_of_30 = my_list.index(30)
print( index_of_30)