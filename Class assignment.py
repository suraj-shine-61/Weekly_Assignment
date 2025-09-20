list=[1,2,3,3,1,2,4,2,4]
unique_element=[]
for num in list:
    if num  not in unique_element:
        unique_element.append(num)
        print(num)


words=['my','name','is','suraj','my','is']
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)