# Multiples Part I
for count in range (1,1001):
    if count % 2 == 0:
        print count

# Multiples Part II
for count in range (1,1000001):
    if count % 5 == 0:
        print count

# Sum List
a=[1,2,5,10,255,3]
sum=0
for count in a:
    sum=sum+count
print sum

# Average List
a=[1,2,5,10,255,3]
sum=0
avg=0
for count in a:
    sum=sum+count
avg=sum/len(a)
print avg