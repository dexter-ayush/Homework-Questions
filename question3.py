threshold = int(input("Enter the threshold you want:\n"))
my_list = [1, 2, 19, 432, 210, 17, 23, 239]
newlist = []
for i in range(len(my_list)):
    if my_list[i] < threshold:
        newlist.append(i)
    
print(newlist)