# newlist=[n for n in range(1,21) if n%2==0]
# print(newlist)
# #Global comprehension

# x='python'
# def myfunc():
#     print('I like ' + x)

# myfunc()

# x='Great' 
# def myfunc():
#     global x 
#     x='awesome'
#     print('I like ' + x)

# myfunc()

# for i in range(3):
#     for j in range(5):
#         print(i*j)
        
        
# #from for loop create a list of even no.
# #using for loop
# even =[]
# for i in range(1,21):
#     if i%2==0:
#         even.append(i)
# print(even)
    
# #using for loop

# even=[n for n in range(1,21) if n%2==0]
# print(even)

# odd=[n for n in range (0,21) if n%2!=0]
# print(odd)


# mylist=['any','am','ivy','airy','a']
# newlist=[]
# for x in mylist:
#     if x.startswith('a') and x.endswith('y'):
#         newlist.append(x)

# print(newlist)


# mylist=['any','am','ivy','airy','a']
# newlist=[x for x in mylist if x.startswith('a') and x.endswith('y')]
# print(newlist)

# mylist=['banana','apple','mango','papaya']
# newlist=[]
# for i in mylist:
#     if i.startswith('b') and i.endswith('a'):
#         newlist.append(i)

# print(newlist)


# l=['a','b','c','d']
# print(l)


# l=l[::-1]
# print(l)


# l=l[::-2]
# print(l)


# l=['a','b','c','d']
# l=l[:2:-1]
# print(l)


# l=['a','b','c','d']
# l=l[::-3]
# print(l)

# l=['a','b','c','d']
# l=l[:1:-1]
# print(l)

# l=['a','b','c','d']
# l=l[:2:-2]
# print(l)


# l=['a','b','c','d']
# l=l[:3:-1]
# print(l)

print("Good night")