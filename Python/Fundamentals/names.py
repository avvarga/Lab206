# # Part I
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# def names(arr):
#     for index in arr:
#         item=""
#         for key,value in index.items():
#             item +=" "+ value
#         print item
# names(students)

# Part II
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def names(arr):
    for key, data in arr.items():
        print key+":"
        y=0
        for value in data:
            x= len(value['first_name'])+len(value['last_name'])
            y +=1
            print y,"-",value['first_name'].upper(),value['last_name'].upper(),"-",x
names(users)