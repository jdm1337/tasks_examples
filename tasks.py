#solve the first task from: https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in range(0,len(a)):
	if a[i] < 5 :
		b.append(a[i])
print(b)