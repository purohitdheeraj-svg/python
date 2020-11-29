def remove_duplicate(A):
		matches = []
		for i in range(len(A)):
		    if A[i] == A[i-1]:
		        matches.append(i)
		for _ in matches:
		    A.pop(matches[0])
		result = ''
		for i in range(len(A)):
		    if A[i] != ',':
		            result += str(A[i])
		return (A).split(' ')
		

A = [1,2,2,3,4,5]
print(remove_duplicate(A))