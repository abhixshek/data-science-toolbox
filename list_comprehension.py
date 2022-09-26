#nested for loops using list comprehension
#lets say we want the tuples (0,6),(0,7),(0,8),(1,6),(1,7),(1,8)

result1 = [(a,b) for a in range(0,2) for b in range(6,9)]

result2 = [num if num%2 == 0 else 10 for num in range(10)]
result3 = [num if num%2 == 0 else 'odd' for num in range(10)]

print(result1)
print(result2)
print(result3)

#dictionary comprehension

fields = ['name', 'school', 'dob']
student = ['abhishek', 'iss','2000-2-25']
dict_student = {i:j for i,j in zip(fields,student)}

print(dict_student)
