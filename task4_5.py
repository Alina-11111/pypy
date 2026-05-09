#for
n = 15
fib_list = []
for i in range(n):
    if i == 0 or i ==1:
        fib_list.append(i)
    else:
        fib_list.append(fib_list[i-1] + fib_list[i-2])
print (*fib_list)

#while
n = 15
fib_list = []
i = 0
while i < n:
    if i == 0 or i ==1:
        fib_list.append(i)
    else:
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    i +=1
print (*fib_list)
