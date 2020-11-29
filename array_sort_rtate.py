''' # Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail


# Write your code here

T = int(input())

list_1 = []
arr_size_int = 0
arr_rotate_int = 0
while T > 0:
    arr_size_rotate = input()
    #print(arr_size_rotate)
    arr_size = arr_size_rotate[0]
    arr_rotate = arr_size_rotate[2]
    #print(type(arr_size), type(arr_rotate))
    arr_size_int = int(arr_size)
    arr_rotate_int = int(arr_rotate)
    #print(arr_size_int, arr_rotate_int)
    for value in range(1,arr_size_int+1):
        list_1.append(value)
        #print(value)

    result = list_1[-arr_rotate_int:] + list_1[:arr_rotate_int+1]
    for value in result:
        print(value, end= " ")
    #for i in range(len(result)):
        #print(list_1[i], end=" ")


    
    T -= 1





# second cases

# Write your code here

T = int(input())

list_1 = []
list_2 = []
while T > 0:
    for i in range(2):
        list_2.append(input())

    arr_size_int = list_2[0][1]
    arr_rotate_int = list_2[0][2]

    list_1.append(list_2[1])
    list_1 = (','.join(list_1)).split()
    #print(list_1)
    
    arr = int(arr_rotate_int)

    result = list_1[-arr:] + list_1[:arr+1]
    #print(result)

    for value in result:
        print(value, end= " ")
    T -= 1
'''



#correct case

for _ in range(int(input())):
    n,k = map(int, input().split())
    k = k%n
    arr = list(map(int,(input().split())))
    arr = arr[-k:] + arr[:k+1]
print(arr)



