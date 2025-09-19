list=[1,2,3,3,1,2,4,2,4]
unique_element=[]
for num in list:
    if num  not in unique_element:
        unique_element.append(num)
        print(num)