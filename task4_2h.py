#for
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
count_even_num = 0
for i, d in enumerate(numbers2):
    if d % 2 ==0:
        count_even_num += 1
       
print (count_even_num)

#while
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
count_even_num = 0
while i < len(numbers2):
    if numbers2[i] % 2 ==0:
        count_even_num += 1
    i+=1  
       
print (count_even_num)