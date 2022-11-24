#1.convert two lists into dict
keys=['Ten','Twenty','Thirty']
values=[10,20,30]
c={}
for i in range(len(values)):
    c[keys[i]]=values[i]
print(c)
#2.delete a list of keys from a dic
sample_dict={'name':'Kelly','age':25,'salary':8000,'city':'New York'}

list=['name','salary']
sample_dict.pop(list)
print(sample_dict)
