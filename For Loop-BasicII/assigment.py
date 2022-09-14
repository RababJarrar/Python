#1
def Biggie_Size(list):
    for x in range(0,len(list),1):
        if (list[x]>0):
            list[x]="big"
    return (list)
print (Biggie_Size([-1, 3, 5, -5]))


#2
def Count_Positives(list):
    count=0
    for x in range(0,len(list),1):
        if (list[x]>0):
            count=count+1
    list[len(list)-1]=count
    return (list)
print (Count_Positives([-1,1,1,1]))


#3
def sum(list):
    z=0
    for x in range(0,len(list),1):
        z=list[x]+z
    return(z)
print (sum([1,2,3,4]))

#4
def avg(list):
    sum=0
    for x in range(0,len(list),1):
        sum=sum+list[x]
    return (sum/len(list))
print (avg([1,2,3,4]))

#5
def length(list):
    return (len(list))
print(length([37,2,1,-9]))

#6
def minimum(list):
    if (len(list)==0):
        return ("false")
    else:
        mini_number=list[0]
        for x in range(0,len(list),1):
            if(list[x]<mini_number):
                mini_number=list[x]
            else:
                continue
        return (mini_number)
print(minimum([37,2,1,-9]))

#7
def max(list):
    if (len(list)==0):
        return ("false")
    else:
        maxi_number=list[0]
        for x in range(0,len(list),1):
            if(list[x]>maxi_number):
                maxi_number=list[x]
            else:
                continue
        return (maxi_number)
print(max([37,2,1,-9]))

#8
def ultimate_analysis(list):
    mydicionary ={'sumTotal':0,'average':0,'minimum':0,'maximum':0,'length':0}
    mydicionary['sumTotal'] = sum(list)
    mydicionary['average'] = avg(list)
    mydicionary['minimum'] = minimum(list)
    mydicionary['maximum'] = max(list)
    mydicionary['length'] = length(list)
    return (mydicionary)

print(ultimate_analysis([37,2,1,-9]))

#9
def Reverse_List(list):
    list.reverse()
    return (list)    
print(Reverse_List([37,2,1,-9]))

# or #9
# def reverse_list(list):
#     for p in range(0,int(len(list)/2),1):
#         temp= list[p]
#         list[p]=list[len(list)-1-p]
#         list[len(list)-1-p]=temp
#     return(list)

# k=reverse_list([37,2,1,-9,10,12])
# print(k)
