N=int(input('vvedite N'))
array=[]
for i in range(N):
    print('Vvedite %d element: ' %i)
    element=int(input())
    array.append(element)
count=0
while count<N:
    count=count+1
    for i in range(N-1):
        if array[i]>array[i+1]:
            b=0
            b=array[i]
            array[i]=array[i+1]
            array[i+1]=b
print(array)


        



