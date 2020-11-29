def group(arr,K):
    index = K - 1
    empty = []

    for value in range(K):
        empty.append(arr[index])
        index -= 1
    result = empty + arr[K:]    
    return result


'''def feed_zero(n):
    string_num = list(n)
    for value in string_num:
        if value == 0:
            string_num.insert(value,5)
    return string_num'''

def sum_of_digits(N):
        res = 0
        while N != 0:
            res = res + N % 10
            N = N // 10 
        return res

print(sum_of_digits(15))
print(group([1,2,3,4,5],3))
#print(feed_zero(1002))