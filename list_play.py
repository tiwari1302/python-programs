list_name=['Shashank','Uday','Riddhi']
list_age=[20,20,19]
list_hobby=['coding','web design','fine arts']

list_of_lists=[list_name,list_age,list_hobby]

#print(len(list_name[2]))
for i in range(len(list_name)):
    print(list_name[i],": ",list_hobby[i],"\n")
print(list_of_lists[0][0][1])
#while(True):
#    print(1)