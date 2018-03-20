words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
new= words.replace("day","month")
print new

x = [2,54,-2,7,12,98]
print "The min is", min(x)
print "The max is", max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print "The first value is", x[0]
print "The last value is", x[len(x)-1:len(x)]

x = [19,2,54,-4,7,12,98,32,10,-3,6]
y = []
x.sort()
for count in range (0,5):
    y.append(x.pop(0))
x.insert (0,y)
print x