with open ('demo.txt') as f:
            r=f.read()
            print(r)

with open ('demo.txt','w')as f:
    r=f.write('hi\n')

with open ('demo.txt','a+') as f:
    r=f.write('from where are you')
    f.seek(0)

with open('demor.txt','r+') as f :
    r=f.write('the file is exclusive creative')
    
    
    
with open ('demo.txt','w+') as f :
    f.write('fine and what about you\n')
    f.seek(0)
    
with open('demo.txt','a+') as f:
    f.write('where are you going?')
    
with open('demo.txt','a+') as f:
    f.write('but now I am fine.')
