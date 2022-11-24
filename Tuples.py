#1.reverse the tuple
tuple1=(10,20,30,40,50)
list1=[]
for i in range(len(tuple1)-1,-1,-1):
    list1.append(tuple1[i])
list1=tuple(list1)
print(list1)
#2.access value 20 from the tuple
Tuple1=('Orange',[10,20,30],(5,15,25))
print(Tuple1[1][1])
#3.unpack the tuple into 4 varibles
print('                    ')
tuple_1=(10,20,30,40)
a,b,c,d=tuple_1[0],tuple_1[1],tuple_1[2],tuple_1[3]
print(a)
print(b)
print(c)
print(d)
