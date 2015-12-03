# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:36:25 2015
@author: sebastianolsson
"""
from  scipy import *
from  pylab import *


print("--------------------------------Task1----------------------")
newfile=open('newfile.txt','w')
newfile.write('1 st line \n')
newfile.write('2nd line \n')
newfile.write('3nd line \n')
newfile.write('4nd line \n')
newfile.write('5nd line \n')
newfile.close()
file=open('newfile.txt','r')
text1=file.read()
text2=file.read()

print(text1)
print(text2)



print("--------------------------------Task2----------------------")
def testfile():
    file=open('newfile.txt','r')
    return file
    
text1=list(testfile())
text2=list(testfile())

print(text1[2])
print(text2)    


print("--------------------------------Task3----------------------")
yearmonthday=[]
kwh=[]

with open('kwh.dat') as f:
    data = [line.split() for line in f.readlines()]
    out = [(yearmonthday.append(k), kwh.append(int(v))) for k, v in data]
    
"""    
for i in kwh:
    print(i)
    
for x in yearmonthday:
    print(x)
"""    
print(yearmonthday)
print(kwh)    


print("--------------------------------Task4----------------------")
yearmonthday.reverse()
kwh.reverse()

print(yearmonthday)
print(kwh)

print("--------------------------------Task5----------------------")
array_kwh = np.array(kwh)
diff_kwh=np.diff(array_kwh)
print(diff_kwh)


print("--------------------------------Task6----------------------")

x_axis=np.arange(0,len(yearmonthday),1)
y_axis=kwh
 
plot(x_axis,y_axis)
title('kwh over months')
xlabel('Month')
ylabel('kwh')
grid(True) 
show()

print("--------------------------------Task7----------------------")

max_energy=max(kwh)
min_energy=min(kwh)

min_index=kwh.index(min(kwh)) #0 because of reverse()
max_index=kwh.index(max(kwh)) #162 because of reverese() 

print("Month with smallest energy consumption",yearmonthday[min_index],"kwh: ",min_energy)
print("Month with largest energy consumption",yearmonthday[max_index],"kwh: ",max_energy)

print("--------------------------------Task8----------------------")

itemindexmin = int(np.where(diff_kwh==min(diff_kwh))[0])
itemindexmax = int(np.where(diff_kwh==max(diff_kwh))[0])

print("Largest consumption decrease",yearmonthday[itemindexmin], "to",yearmonthday[itemindexmin+1], " kwh:",min(diff_kwh) )
print("Largest consumption increase",yearmonthday[itemindexmax], "to",yearmonthday[itemindexmax+1], " kwh:",max(diff_kwh) )

print("--------------------------------Task9----------------------")
mean_kwh=mean(kwh)
print("Mean value",mean_kwh)



