def countdown(num):
    for x in range(num,-1,-1):
        print(x)
countdown(5)


def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([1,2]))


def first_plus_length(list):
    return (list[0]+len(list))
print (first_plus_length([1,2,5,4,5]))


def greater(list):
    if (len(list)<3):
       return False 
    z=0
    newList = []
    for x in range(0,len(list),1):
        if(list[x]>list[1]):
            newList.append(list[x])
            z=z+1
    print(z)
    return newList
print(greater([5,2,3,2,1,4]))


def length_and_value(size,value):
    newList = []
    for i in range(0,size,1):
        newList.append(value)
    return newList
print(length_and_value(3,8))   




