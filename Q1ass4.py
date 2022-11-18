print('Welcome')
name=input('Please,enter your name')
age=input('enter your age')
address=input('enter your address')
if age.isdigit()and not age.isspace() and type(name)is str and not name.isspace()and type(address)is str and not address.isspace():
    age=int(age)
    print('Hello Mr/Ms',{name},'age',{age},'located in',{address},'.',' \nthanks for beening one of our communty,',' \t enjoy')
else:print('There is wrong valrue, Try again and enter correctly ')
