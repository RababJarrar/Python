# #3
# def sum(list):
#     z=0
#     for x in range(0,len(list),1):
#         z=list[x]+z
#     return(z)
# print (sum([1,2,3,4]))

# #4
# def avg

# #5
# def length(list):
#     return (len(list))
# print(length([37,2,1,-9]))

#6
def minimum(list):
    for x in range(0,len(list),1):
        if list[x]<list[x+1]:
            minimum_number=list[x]
    return(minimum_number)
print(minimum([37,2,1,-9])
