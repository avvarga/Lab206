word_list = ['hello','world','my','name','is','Anna']
char = "o"
found=[]
for index in word_list:
    if index.find(char)!=-1:
        found.append(index)
print found