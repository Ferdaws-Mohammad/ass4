n1= input('Please,Enter the first number')
n2= input('Please,Enter the second number')
n3= input('Please,Enter the third number')
n4= input('Please,Enter the fourth number')
n5= input('Please,Enter the fifth number')
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
arr=[n1,n2,n3,n4,n5]
if arr[0]>arr[1] and arr[0]>arr[2]  and arr[0]>arr[3]  and arr[0]>arr[4]:
    print('Max number=', arr[0])
elif arr[1]>arr[0] and arr[1]>arr[2]  and arr[1]>arr[3]  and arr[1]>arr[4]:
    print('Max number=', arr[1])
elif arr[2] > arr[0] and arr[2] > arr[1] and arr[2] > arr[3] and arr[2]> arr[4]:
    print('Max number=', arr[2])
elif arr[3] > arr[0] and arr[3] > arr[1] and arr[3] > arr[2] and arr[3]> arr[4]:
    print('Max number=', arr[3])
else:print('Max number=',arr[4])
