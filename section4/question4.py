day_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for ele in day_list:
    if len(ele) > 2 and ele[0] == ele[-1]:
        count+=1
print(count)
