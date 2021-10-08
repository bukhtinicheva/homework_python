array={1,6,8,4,3,0,5}
temp=0
def bubble(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
print(array)