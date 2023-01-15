my_list = [2,2,4,5,6,7,4,5]
new_list = []

for ele in my_list:
    if ele not in new_list:
        new_list.append(ele)
print(new_list)