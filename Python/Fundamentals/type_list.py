x=['magical unicorns',19,'hello',98.98,'world']
y=[]
sum=0
for count in range(len(x)):
    if isinstance (x[count],int):
        sum=sum+x[count]
    elif isinstance (x[count],float):
        sum=sum+x[count]
    elif isinstance (x[count],str):
        y.append(x[count])
if sum == 0:
    print "The list your entered is of string type"
    print "String:", y
elif y == []:
    print "The list you entered is of integer type"
    print "Sum:", sum 
else:
    print "The list you entered is of mixed type"
    print "String:" , y
    print "Sum:" , sum