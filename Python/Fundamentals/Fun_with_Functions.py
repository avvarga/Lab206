# Odds and Evens
def odds_evens(a,b):
    for index in range(a,b):
        if index%2 == 0:
            print "The number is "+str(index)+". This number is odd"
        else:
            print "The number is "+str(index)+". This number is even"
# odds_evens(1,2001)

# Multiply
def multiply(arr,b):
    for index in range(len(arr)):
        arr[index]*= b
    return arr
# print multiply([2,4,10,16],5)

# Hacker Challenge
def layered_multiples(arr):
    main_list=[]
    for index in arr:
        sub_list = []
        for count in range(index):
            sub_list.append(1)
        main_list.append(sub_list)
        sub_list=[]      
    return main_list
x = layered_multiples(multiply([2,4,5],3))
print x