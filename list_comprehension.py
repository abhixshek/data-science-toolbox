#nested for loops using list comprehension
#lets say we want the tuples (0,6),(0,7),(0,8),(1,6),(1,7),(1,8)

result = [(a,b) for a in range(0,2) for b in range(6,9)]
