#1.disblay numbers from a list using loop
numbers=[12,75,150,180,145,525,50]
for item in numbers:
    if item > 500:
       break
    if item > 150:
        continue
    if item%5==0:
        print(item)
#2.disbly meesage done
if True:
   for i in range(5):
    print(i)
   else:
        print('Done')
#3. reverse integer number

n=76542
r=0
rev_nu=0
while n!=0:
    r=n%10
    rev_nu=rev_nu*10+r
    n=n/10

print(rev_nu)


