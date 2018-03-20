# Part I
# def draw_stars(arr):
#     for index in arr:
#         x=""
#         for count in range (index):
#             x+=('*')
#         print x
# draw_stars([4,6,1,3,5,7,25])

# Part II
def draw_stars(arr):
    for index in arr:
        x=""
        if isinstance (index,int):
            for count in range (index):
                x+=('*')
        elif isinstance (index,str):
            for count in range (len(index)):
                x+=index[0]
        print x

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])